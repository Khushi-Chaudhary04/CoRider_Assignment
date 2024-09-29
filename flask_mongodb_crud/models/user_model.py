from bson.objectid import ObjectId

class UserModel:
    def __init__(self, db):
        self.collection = db['users']

    # Create a new user
    def create_user(self, data):
        return self.collection.insert_one(data).inserted_id

    # Get a user by ID
    def get_user(self, user_id):
        return self.collection.find_one({"_id": ObjectId(user_id)})

    # Get all users
    def get_all_users(self):
        return list(self.collection.find())

    # Update a user by ID
    def update_user(self, user_id, data):
        return self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})

    # Delete a user by ID
    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": ObjectId(user_id)})
