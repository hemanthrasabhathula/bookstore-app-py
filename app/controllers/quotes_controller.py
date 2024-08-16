from flask import Blueprint, request
from app.services.book_service import get_book_by_details_service
from app.utils.response import success_response, error_response, created_response
from app.services.quote_service import add_quote_service
from bson.json_util import dumps
quotes_bp = Blueprint('quotes', __name__)


@quotes_bp.route('/quotes', methods=['POST'])
def insert_quotes():
    try:
        request_data = request.get_json()
        currentBook = None
        for quoteData in request_data:
            if 'bookTitle' in quoteData and 'quote' in quoteData:

                if currentBook == quoteData['bookTitle']:
                    currentBook = quoteData['bookTitle']
                else:
                    currentBook = get_book_by_details_service(
                        {'title': quoteData['bookTitle']})
                if currentBook == None:
                    return error_response(message='Book not found')

                added_quote = add_quote_service(quoteData, currentBook)
                if added_quote == None:
                    return error_response(message='Failed to add quote')
            else:
                return error_response(message='Invalid quote data')
        return created_response(message='Quotes added successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to add quotes')
