### Steps to Run Your Application

1. **Set up MongoDB Atlas**:
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create an account.
   - Create a cluster, and under *Database Access*, create a new user 
   - Get the connection string (replace `<password>` with your actual password).

2. **Configure your project**:
   - Place your MongoDB Atlas connection string in `app.py` (in the `MongoClient` initialization part).

3. **Install dependencies**:
   - Run the following command to install all the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the application**:
   - Start the Flask app by running:
     ```bash
     python app.py
     ```

5. **Testing in Postman**:
   - Open Postman and start making requests:
     - `GET /users` - to list all users.
     - `POST /users` - to create a new user (pass `name`, `email`, `password` in the body as JSON).
     - `GET /users/<id>` - to get a specific user by ID.
     - `PUT /users/<id>` - to update a specific user.
     - `DELETE /users/<id>` - to delete a specific user.

