from flask import Blueprint
from bson.json_util import dumps
from flask import request
from app.services.user_service import get_all_users, get_user_by_id, add_user, get_user_by_email
from app.utils.response import success_response, error_response

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/register', methods=['POST'])
def register_user():

    try:
        user_data = request.get_json()
        if ('username' not in user_data or 'email' not in user_data or 'password' not in user_data):
            return error_response(message='Invalid request data')
        exist_user = get_user_by_email(user_data['email'])
        if (exist_user is not None):
            return error_response(message='User already exists', status=409)
        else:
            add_user(user_data)
            if (user_data['_id'] is None):
                return error_response(message='Failed to register user')
            else:
                return success_response(data=user_data, message='User registered successfully')

    except Exception as e:
        return error_response(data=dumps(str(e)), message='Error registering user')
