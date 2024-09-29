from flask_restful import Resource, reqparse
from flask import jsonify
from models.user_model import UserModel

class UserResource(Resource):
    def __init__(self, db):
        self.db = UserModel(db)

    # Get all users
    def get(self, user_id=None):
        if user_id:
            user = self.db.get_user(user_id)
            if user:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string
                return jsonify(user)
            return {"message": "User not found"}, 404
        else:
            users = self.db.get_all_users()
            for user in users:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string
            return jsonify(users)

    # Create a new user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        user_data = {
            'name': args['name'],
            'email': args['email'],
            'password': args['password']
        }

        user_id = self.db.create_user(user_data)
        return {"message": "User created", "user_id": str(user_id)}, 201

    # Update an existing user
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('email')
        parser.add_argument('password')
        args = parser.parse_args()

        update_data = {k: v for k, v in args.items() if v}

        if update_data:
            updated = self.db.update_user(user_id, update_data)
            if updated.modified_count:
                return {"message": "User updated"}, 200
            return {"message": "User not found"}, 404
        return {"message": "No data provided"}, 400

    # Delete an existing user
    def delete(self, user_id):
        deleted = self.db.delete_user(user_id)
        if deleted.deleted_count:
            return {"message": "User deleted"}, 200
        return {"message": "User not found"}, 404
