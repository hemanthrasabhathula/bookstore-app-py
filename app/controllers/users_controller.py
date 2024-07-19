from flask import Blueprint
from bson.json_util import dumps
from flask import request
from app.services.user_service import get_all_users, get_user_by_id, add_user, get_user_by_email
from app.utils.response import success_response, error_response
from bcrypt import hashpw, gensalt, checkpw
from app.utils.helper import pop
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
            user_data['password'] = hashpw(
                user_data['password'].encode('utf-8'), gensalt())
            pop(user_data, 'confirmpassword')
            add_user(user_data)
            if (user_data['_id'] is None):
                return error_response(message='Failed to register user')
            else:
                return success_response(message='User registered successfully')

    except Exception as e:
        return error_response(data=dumps(str(e)), message='Error registering user')


@auth_bp.route('/auth/login', methods=['POST'])
def authenticate_user():
    try:
        login_data = request.get_json()
        if ('email' not in login_data or 'password' not in login_data):
            return error_response(message='Invalid request data', status=400)
        exist_user = get_user_by_email(login_data['email'])
        if (exist_user is None):
            return error_response(message='Email Id not found', status=404)
        else:
            if (checkpw(login_data['password'].encode('utf-8'), exist_user['password'])):
                pop(exist_user, 'password')
                return success_response(data=exist_user, message='User authenticated successfully', status=200)
            else:
                return error_response(message='Incorrect password', status=401)
    except Exception as e:
        return error_response(data=dumps(str(e)), message='Error authenticating user', status=500)
