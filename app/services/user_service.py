from app.models.user import User
from app.utils.helper import pop


def get_all_users():
    return User.get_all_users()


def get_user_by_id(user_id):
    return User.get_user_by_id(user_id)


def get_user_by_email(email):
    if (email is not None):
        email = email.lower()
    else:
        return None
    return User.get_user_by_email(email)


def add_user(user):
    user['email'] = user['email'].lower()
    user = pop(user, 'confirmPassword')
    return User.add_user(user)
