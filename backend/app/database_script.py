import psycopg2
from constant import database_host


def data_insert():
    # List of quotes
    quotes = [
        "The only way to do great work is to love what you do.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "In the middle of every difficulty lies opportunity.",
        "Don't watch the clock; do what it does. Keep going.",
        "The harder I work, the luckier I get.",
        "Strive not to be a success, but rather to be of value.",
        "The best revenge is massive success.",
        "The secret to getting ahead is getting started.",
        "You are never too old to set another goal or to dream a new dream.",
        "The only limit to our realization of tomorrow will be our doubts of today.",
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
        "It does not matter how slowly you go as long as you do not stop.",
        "Success is not the key to happiness. Happiness is the key to success.",
        "The only place where success comes before work is in the dictionary."
    ]

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=database_host,
        port="5432",
        database="quotes_show",
        user="root",
        password="root12345"
    )

    # Create a cursor
    cursor = conn.cursor()

    # Check if the quotes table exists
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'quotes'
        )
    """)
    table_exists = cursor.fetchone()[0]

    if table_exists:
        # Fetch existing quotes from the table
        cursor.execute("SELECT quote FROM quotes")
        existing_quotes = set(cursor.fetchall())

        # Filter new quotes that are not already in the table
        new_quotes = [quote for quote in quotes if quote not in existing_quotes]

        if new_quotes:
            # Insert the new quotes into the table
            for quote in new_quotes:
                cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (quote,))

            # Commit the changes
            conn.commit()
            print("New quotes inserted into the database.")
        else:
            print("All quotes already exist in the database.")
    else:
        # Create the quotes table
        cursor.execute("""
            CREATE TABLE quotes (
                id SERIAL PRIMARY KEY,
                quote TEXT
            )
        """)

        # Insert quotes into the table
        for quote in quotes:
            cursor.execute("INSERT INTO quotes (quote) VALUES (%s)", (quote,))

        # Commit the changes
        conn.commit()
        print("Quotes table created and quotes inserted into the database.")

    # Close the cursor and connection
    cursor.close()
    conn.close()
