from app.utils.database import db
from bson.objectid import ObjectId
from bson.json_util import dumps


class Branch:
    collection = db.Branches

    @staticmethod
    def get_all_branches():
        return list(Branch.collection.find({}))

    @staticmethod
    def get_branch_by_id(branch_id):
        return Branch.collection.find_one({"_id": ObjectId(branch_id)})

    @staticmethod
    def add_branch(branch):
        return Branch.collection.insert_one(branch).inserted_id

    @staticmethod
    def del_branch_by_id(branch_id):
        return Branch.collection.delete_one({"_id": ObjectId(branch_id)}).deleted_count
