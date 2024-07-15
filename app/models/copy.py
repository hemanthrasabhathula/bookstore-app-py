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

    @staticmethod
    def get_available_copies(book_id, branch_id, status, count):
        if not isinstance(book_id, ObjectId):
            book_id = ObjectId(book_id)
        if not isinstance(branch_id, ObjectId):
            branch_id = ObjectId(branch_id)
        return list(Copy.collection.find({"bookId": book_id, "branchId": branch_id, "status": status}).limit(count))

    @staticmethod
    def update_copy(copy_id, data):
        return Copy.collection.update_one({"_id": copy_id}, {"$set": data})
