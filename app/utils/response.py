
from flask import Response
from bson.json_util import dumps
from flask import jsonify


def success_response(message, data):

    return Response(response=convert_response(message, data), status=200, headers={'message': message}, mimetype='application/json')


def error_response(message, data):

    return Response(response=convert_response(message, data), status=400, headers={'message': message}, mimetype='application/json')


def created_response(message, data):

    return Response(response=convert_response(message, data), status=201, headers={'message': message}, mimetype='application/json')


def deleted_response(message):

    return Response(response=convert_response(message), status=200, headers={'message': message}, mimetype='application/json')


def convert_response(message, data=None):
    response_data = {}
    if data is not None:
        response_data['data'] = data
    if message is not None:
        response_data['message'] = message
    return dumps(response_data)
