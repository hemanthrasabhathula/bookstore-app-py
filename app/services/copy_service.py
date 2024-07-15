from app.models.copy import Copy


def get_all_copies():
    return Copy.get_all_copies()


def get_copy_by_id(copy_id):
    return Copy.get_copy_by_id(copy_id)


def add_copies(copies):
    return Copy.add_copies(copies)


def get_available_copies_service(book_id, branch_id, status, count):
    return Copy.get_available_copies(book_id, branch_id, status, count)


def updated_copy(copy_id, data):
    return Copy.update_copy(copy_id, data)
