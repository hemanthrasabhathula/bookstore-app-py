from app.utils.database import db
from bson.objectid import ObjectId
from bson.json_util import dumps


class Book:
    collection = db.Books

    @staticmethod
    def get_all_books():
        books = list(Book.collection.find({}))
        return dumps(books)

    @staticmethod
    def get_book_by_id(book_id):
        book = Book.collection.find_one({"_id":  ObjectId(book_id)})
        return dumps(book)
