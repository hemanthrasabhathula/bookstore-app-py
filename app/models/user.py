from app.utils.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId


class User:
    collection = db.Users

    @staticmethod
    def get_all_users():
        return list(User.collection.find({}))

    @staticmethod
    def get_user_by_id(user_id):
        return User.collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def get_user_by_email(email):
        return User.collection.find_one({"email": email})

    @staticmethod
    def add_user(user):
        return User.collection.insert_one(user)
