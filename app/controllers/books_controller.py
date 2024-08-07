from app.utils.helper import pop_id, push_id
from flask import Blueprint
from app.services.book_service import get_books, get_book_by_id, add_new_book, del_book_by_id, get_book_by_title_service, get_book_by_title_pattern_service, get_book_by_details_service
from app.services.copy_service import get_copies_by_book_id_service, get_borrowed_copies_by_book_id_service, get_available_copies_service, delete_copies_by_book_id_service
from app.utils.response import success_response, error_response
from bson.json_util import dumps
from flask import request
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
        if (book == None):
            return error_response(message='Book not found')
        else:
            return success_response(data=book, message='Book retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve book')


@books_bp.route('/books/bookbytitle/<title>', methods=['GET'])
def get_book_by_title(title):
    try:
        book = get_book_by_title_service(title)
        if (book == None):
            return error_response(message='Book not found')
        else:
            return success_response(data=book, message='Book retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve book')


@books_bp.route('/books/bookbytitlepattern/<title_pattern>', methods=['GET'])
def get_book_by_title_pattern(title_pattern):
    try:
        books = get_book_by_title_pattern_service(title_pattern)
        if (books == None):
            return error_response(message='Book not found')
        else:
            return success_response(data=books, message='Book retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve book')


@books_bp.route('/books/bookbydetails', methods=['POST'])
def get_book_by_details():
    try:
        request_data = request.get_json()
        book_data = {}
        if 'title' in request_data and 'ISBN' in request_data:
            book_data = get_book_by_details_service(request_data)
        else:
            return error_response(message='request details are not found')

        if (book_data == None):
            return error_response(message='Book not found')
        else:
            return success_response(data=book_data, message='Book retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve book')


@books_bp.route('/book', methods=['POST'])
def add_book():
    try:
        book = pop_id(request.get_json())
        book_id = add_new_book(book)
        inserted_book = push_id(request.get_json(), book_id)
        return success_response(data=inserted_book, message='Book added successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to add book')


@books_bp.route('/book/<book_id>', methods=['DELETE'])
def del_book(book_id):
    try:
        if (get_book_by_id(book_id) == None):
            return error_response(message='Book not found')
        if (len(get_borrowed_copies_by_book_id_service(book_id)) > 0):
            return error_response(message='Book has borrowed copies. this book cannot be deleted')
        else:
            if (delete_copies_by_book_id_service(book_id) >= 1):
                if (del_book_by_id(book_id) == 1):
                    return success_response(message='Book deleted successfully')
                else:
                    return error_response(message='Failed to delete book')
            else:
                return error_response(message='Failed to delete book copies')

        # if (del_book_by_id(book_id) == 1):
        #     return success_response(message='Book deleted successfully')
        # else:
        #     return error_response(message='Failed to delete book')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to delete book')
