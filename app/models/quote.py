from app.utils.database import db
from bson.json_util import dumps
from bson.objectid import ObjectId


class Quote:
    collection = db.Quotes

    @staticmethod
    def add_quote(quote):
        return Quote.collection.insert_one(quote).inserted_id

    def get_quotes(book_id):
        return list(Quote.collection.find(book_id))
