from app.utils.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import DESCENDING


class Transaction:
    collection = db.Transactions

    @staticmethod
    def get_all_transactions():
        return list(Transaction.collection.find({}).sort('borrowedDate', DESCENDING))

    @staticmethod
    def get_all_user_transactions(user_id):
        return list(Transaction.collection.find({"userId": ObjectId(user_id)}))

    @staticmethod
    def get_copy_transactions(copy_id):
        return Transaction.collection.find_one({'copyId': copy_id})

    def get_copy_transactions_by_status(copy_id, status):
        return Transaction.collection.find_one({'copyId': copy_id, 'status': status})

    @staticmethod
    def add_transactions(transactions):
        return Transaction.collection.insert_many(transactions)

    @staticmethod
    def update_transaction(transaction_id, data):
        return Transaction.collection.update_one({"_id": transaction_id}, {"$set": data})
