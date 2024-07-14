from flask import Blueprint
from bson.json_util import dumps
from flask import request
from app.utils.helper import pop_id, push_id, pop
from app.services.copy_service import get_all_copies, get_copy_by_id, add_copies
from app.services.book_service import add_new_book
from app.utils.response import success_response, error_response, created_response
from bson.objectid import ObjectId
import copy
copies_bp = Blueprint('copies', __name__)


@copies_bp.route('/copies', methods=['GET'])
def get_copies():
    try:
        copies = get_all_copies()
        return success_response(data=copies, message='Copies retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve copies')


@copies_bp.route('/copy/<copy_id>', methods=['GET'])
def get_copy(copy_id):
    try:
        copy = get_copy_by_id(copy_id)
        if (copy == None):
            return error_response(message='Copy not found')
        else:
            return success_response(data=copy, message='Copy retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve copy')


@copies_bp.route('/addcopy', methods=['POST'])
def add_copy():
    try:
        request_data = request.get_json()
        data = copy.deepcopy(request_data)
        book_data = pop(request_data, 'branchCopy')
        book_id = add_new_book(book_data)
        if (book_id == None):
            return error_response(message='Failed to add book')
        else:
            copies_data = []
            branch_copies = data['branchCopy']
            print(branch_copies)
            for branch_copy in branch_copies:
                for i in range(int(branch_copy['copies'])):
                    copy_data = {
                        'bookId': ObjectId(book_id),
                        'branchId': ObjectId(branch_copy['branch']),
                        'status': 'available'
                    }
                    copies_data.append(copy_data)
            added_copies = add_copies(copies_data)
            if (added_copies != None):
                return created_response(message='Copies added successfully', data=copies_data)
            else:
                return error_response(message='Failed to add copies')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to add copies')
