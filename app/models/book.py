from app.utils.database import db
from bson.objectid import ObjectId
from bson.json_util import dumps


class Book:
    collection = db.Books

    @staticmethod
    def get_all_books():
        return list(Book.collection.find({}))

    @staticmethod
    def get_book_by_id(book_id):
        return Book.collection.find_one({"_id":  ObjectId(book_id)})

    @staticmethod
    def insert_book(book):
        return Book.collection.insert_one(book).inserted_id

    @staticmethod
    def delete_book_by_id(book_id):
        return Book.collection.delete_one({"_id": ObjectId(book_id)}).deleted_count
