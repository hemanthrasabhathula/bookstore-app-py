from flask import Blueprint
from app.services.branch_service import get_branch_by_id, get_branches, insert_branch, del_branch_by_id
from app.utils.response import success_response, error_response, created_response
from bson.json_util import dumps
from flask import request
from app.utils.helper import pop_id, push_id

branches_bp = Blueprint('branches', __name__)


@branches_bp.route('/branches', methods=['GET'])
def get_all_branches():
    try:
        branches = get_branches()
        return success_response(data=branches, message='Branches retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve branches')


@branches_bp.route('/branch/<branch_id>', methods=['GET'])
def get_branch(branch_id):
    try:
        branch = get_branch_by_id(branch_id)
        if (branch == None):
            return error_response(message='Branch not found')
        else:
            print(branch)
            return success_response(data=branch, message='Branch retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve branch')


@branches_bp.route('/branch', methods=['POST'])
def add_branch():
    try:
        branch = pop_id(request.get_json())
        _id = insert_branch(branch)
        return created_response(message='Branch added successfully', data=push_id(request.get_json(), _id))
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to add branch')


@branches_bp.route('/branch/<branch_id>', methods=['DELETE'])
def delete_branch(branch_id):
    try:
        if (del_branch_by_id(branch_id) == 1):
            return success_response(message='Branch deleted successfully')
        else:
            return error_response(message='Failed to delete branch')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to delete branch')
