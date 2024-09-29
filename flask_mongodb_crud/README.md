# Flask MongoDB CRUD Application

This is a Flask application that performs CRUD operations on a MongoDB database for a User resource using a REST API.

## Setup

1. Clone the repository.
2. Ensure MongoDB is running locally or use MongoDB Atlas.
3. Build and run the Docker container:

```bash
docker build -t flask-mongodb-crud .
docker run -p 5000:5000 flask-mongodb-crud
