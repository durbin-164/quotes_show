# Use an official Node.js runtime as the base image
FROM node:14.17.1-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install NPM dependencies
RUN npm install

# Copy the rest of the frontend files to the working directory
COPY . .

# Expose the desired port (adjust if necessary)
EXPOSE 3000

# Set the command to run the frontend server
CMD ["npm", "start"]
