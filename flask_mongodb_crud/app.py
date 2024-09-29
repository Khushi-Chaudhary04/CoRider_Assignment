from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
from resources.user import UserResource

app = Flask(__name__)
api = Api(app)

# MongoDB Atlas connection setup (replace with your credentials)
client = MongoClient("mongodb://Khushi:<password>@cluster0-shard-00-00.mongodb.net:27017,myFirstDatabase?ssl=true&replicaSet=atlas-xyz-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client['myFirstDatabase']

# Add user resource to API
api.add_resource(UserResource, '/users', '/users/<string:user_id>', resource_class_args=[db])

if __name__ == '__main__':
    app.run(debug=True)
