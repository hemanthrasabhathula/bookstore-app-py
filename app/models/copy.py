from app.utils.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId


class Copy:
    collection = db.Copies

    @staticmethod
    def get_all_copies():
        return list(Copy.collection.find({}))

    @staticmethod
    def get_copy_by_id(copy_id):
        return Copy.collection.find_one({"_id": ObjectId(copy_id)})

    @staticmethod
    def add_copies(copies):
        return Copy.collection.insert_many(copies).inserted_ids
