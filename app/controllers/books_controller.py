from flask import Blueprint
from app.services.book_service import get_books, get_book_by_id
from app.utils.response import success_response, error_response
from bson.json_util import dumps
books_bp = Blueprint('books', __name__)


@books_bp.route('/books', methods=['GET'])
def get_all_books():
    try:
        books = get_books()
        return success_response(data=books, message='Books retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve books')


@books_bp.route('/book/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
        book = get_book_by_id(book_id)
        return success_response(data=book, message='Book retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve book')
