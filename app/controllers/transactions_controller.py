import datetime
from app.services.copy_service import add_copies, get_copy_by_id, get_all_copies, get_available_copies_service, updated_copy
from app.models.copy import Copy
from flask import Blueprint, request
from app.services.transaction_service import get_all_transactions, get_all_user_transactions, add_transactions
from app.utils.response import success_response, error_response, created_response
from bson.json_util import dumps
from bson.objectid import ObjectId


transactions_bp = Blueprint('transactions', __name__)


@transactions_bp.route('/transactions', methods=['GET'])
def get_transactions():
    try:
        transactions = get_all_transactions()
        return success_response(data=transactions, message='Transactions retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve transactions')


@transactions_bp.route('/transactions/<user_id>', methods=['GET'])
def get_user_transactions(user_id):
    try:
        transactions = get_all_user_transactions(user_id)
        return success_response(data=transactions, message='User Transactions retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve transactions')


@transactions_bp.route('/transactions', methods=['POST'])
def add_transaction():
    try:
        data = request.get_json()
        for entry in data:
            book_id = entry['book']['_id']['$oid']
            book_title = entry['book']['title']
            book_author = entry['book']['author']
            for branch in entry['branches']:
                branch_id = branch['_id']['$oid']
                branch_name = branch['name']
                count = branch['count']

                copies_to_borrow = get_available_copies_service(
                    book_id, branch_id, 'available', count)

                transaction_records = []

                for copy in copies_to_borrow:
                    copy_id = copy['_id']
                    updated_copy(copy_id, {"status": "borrowed"})
                    transaction_record = {
                        'bookId': ObjectId(book_id),
                        'bookName': book_title,
                        'author': book_author,
                        'branchId': ObjectId(branch_id),
                        'branchName': branch_name,
                        'copyId': copy_id,
                        'status': 'borrowed',
                        'borrowedDate': datetime.datetime.now(),
                        'dueDate': datetime.datetime.now() + datetime.timedelta(days=7),
                        'lateFee': 0
                    }
                    transaction_records.append(transaction_record)

                if (len(transaction_records) == count):
                    add_transactions(transaction_records)
                else:
                    return error_response(message='Failed to borrow books')

        return created_response(message='Books borrowed successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to borrow books')
