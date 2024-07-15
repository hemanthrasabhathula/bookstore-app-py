from app.utils.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId


class Transaction:
    collection = db.Transactions

    @staticmethod
    def get_all_transactions():
        return list(Transaction.collection.find({}))

    @staticmethod
    def get_all_user_transactions(user_id):
        return list(Transaction.collection.find({"userId": user_id}))

    @staticmethod
    def add_transactions(transactions):
        return Transaction.collection.insert_many(transactions)
