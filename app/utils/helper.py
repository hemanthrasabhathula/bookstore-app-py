from bson.objectid import ObjectId


def pop(Object, key):
    Object.pop(key, None)
    return Object


def pop_id(Object):
    Object.pop('_id', None)
    return Object


def push_id(Object, _id):
    if '_id' in Object:
        Object['_id'] = ObjectId(_id)
    return Object
