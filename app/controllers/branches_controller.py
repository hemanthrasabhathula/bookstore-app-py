from flask import Blueprint
from app.services.branch_service import get_branch_by_id, get_branches
from app.utils.response import success_response, error_response
from bson.json_util import dumps

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
        return success_response(data=branch, message='Branch retrieved successfully')
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Failed to retrieve branch')
