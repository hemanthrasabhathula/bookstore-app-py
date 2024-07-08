from app.utils.database import db
from bson.objectid import ObjectId
from bson.json_util import dumps


class Branch:
    collection = db.Branches

    @staticmethod
    def get_all_branches():
        branches = list(Branch.collection.find({}))
        return dumps(branches)

    @staticmethod
    def get_branch_by_id(branch_id):
        branch = Branch.collection.find_one({"_id": ObjectId(branch_id)})
        return dumps(branch)
