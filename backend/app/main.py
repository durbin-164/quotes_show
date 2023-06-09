from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from random import choice
import asyncpg
import aioredis
from database_script import data_insert
import constant
import random



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Quote(BaseModel):
    quote: str
    source: str

@app.on_event("startup")
async def startup():
    # Connect to the PostgreSQL database
    app.db = await asyncpg.connect(
        user='root',
        password='root12345',
        database='quotes_show',
        host=constant.database_host
    )

    # Connect to Redis cache
    app.redis = await aioredis.from_url(f"redis://{constant.redis_host}")

    data_insert()

@app.on_event("shutdown")
async def shutdown():
    # Close the database connection
    await app.db.close()

    # Close the Redis cache connection
    app.redis.close()
    await app.redis.wait_closed()

@app.get("/api/quote", response_model=Quote)
async def get_random_quote():
    # Check if the quote exists in the cache
    random_number = random.randint(1, constant.total_quotes)
    cache_key = f"random_quote_{random_number}"

    quote = await app.redis.get(cache_key)
    if quote:
        return Quote(quote=quote.decode(), source="Cache")

    # Fetch all quotes from the database
    quotes = await app.db.fetch("SELECT quote FROM quotes")

    # Choose a random quote
    random_quote = choice(quotes)

    # Store the random quote in the cache
    await app.redis.setex(cache_key, constant.cache_ttl, random_quote["quote"])

    return Quote(quote=random_quote['quote'], source="DB")
