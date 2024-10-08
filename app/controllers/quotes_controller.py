from bson import ObjectId
from flask import Blueprint, request
from app.services.book_service import get_book_by_details_service, get_book_by_id
from app.utils.response import success_response, error_response, created_response
from app.services.quote_service import add_quote_service, get_quotes_by_book_service
from bson.json_util import dumps
quotes_bp = Blueprint('quotes', __name__)


@quotes_bp.route('/quotes/<book_id>', methods=['GET'])
def get_quotes_by_book(book_id):
    try:
        quotes_data = get_quotes_by_book_service(book_id)
        if quotes_data == None or not quotes_data:
            return error_response(message="Failed to fetch the quotes")
        return success_response(data=quotes_data, message='quotes retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(e), message="Error while fetching quotes")


@quotes_bp.route('/quotes/<book_id>', methods=['POST'])
def insert_quotes(book_id):

    try:
        request_data = request.get_json()
        book_data = get_book_by_id(book_id)

        if book_data == None:
            return error_response(message='Book not found')
        for quoteData in request_data:
            added_quote = add_quote_service(quoteData, book_data)
            if added_quote == None:
                return error_response(message='Failed to add quote')
        return created_response(message='Quotes added successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to add quotes')
