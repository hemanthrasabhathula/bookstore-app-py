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
    def get_book_by_title(title):
        return Book.collection.find_one({"title": title})

    @staticmethod
    def find_books_by_title_pattern(title_pattern):
        return list(Book.collection.find({'title': {'$regex': title_pattern, '$options': 'i'}}))

    @staticmethod
    def get_book_by_details(details):
        return Book.collection.find_one(details)

    @staticmethod
    def insert_book(book):
        return Book.collection.insert_one(book).inserted_id

    @staticmethod
    def delete_book_by_id(book_id):
        return Book.collection.delete_one({"_id": ObjectId(book_id)}).deleted_count
