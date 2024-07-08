
from flask import Response


def success_response(data, message):

    return Response(response=data.encode('utf-8'), status=200, headers={'message': message}, mimetype='application/json')


def error_response(data, message):

    return Response(response=data.encode('utf-8'), status=400, headers={'message': message}, mimetype='application/json')
