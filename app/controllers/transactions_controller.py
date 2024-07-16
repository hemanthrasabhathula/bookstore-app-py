import datetime
from app.services.copy_service import add_copies, get_copy_by_id, get_all_copies, get_available_copies_service, updated_copy
from app.models.copy import Copy
from flask import Blueprint, request
from app.services.transaction_service import get_all_transactions, get_all_user_transactions, add_transactions, get_copy_transactions, update_transaction, get_copy_transactions_by_status
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


@transactions_bp.route('/transactions/copy/<copy_id>', methods=['GET'])
def get_transactions_by_copy_id(copy_id):
    try:
        copy_transaction = get_copy_transactions(ObjectId(copy_id))
        if (copy_transaction == None):
            return error_response(message='Transaction of the Copy not found')
        return success_response(data=copy_transaction, message='Copy Transaction retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve copy transaction')


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
                        'returnDate': None,
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


@transactions_bp.route('/transactions/return/<copy_id>', methods=['PUT'])
def return_transaction(copy_id):
    try:
        copy = get_copy_by_id(copy_id)
        if (copy == None):
            return error_response(message='Copy not found')
        else:
            modified_copy_count = updated_copy(
                copy['_id'], {"status": "available"}).modified_count
            if (modified_copy_count == 1):
                copy_transaction = get_copy_transactions_by_status(
                    copy['_id'], 'borrowed')
                modified_transaction_count = update_transaction(copy_transaction['_id'], {
                    "status": "returned",
                    "returnDate": datetime.datetime.now()
                }).modified_count
                if (modified_transaction_count == 1):
                    return success_response(message='Copy returned successfully')
                return error_response(message='Failed to update transaction status')
            return error_response(message='Failed to return copy')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to return copy')
