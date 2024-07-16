from app.models.book import Book


def get_books():
    return Book.get_all_books()


def get_book_by_id(book_id):
    return Book.get_book_by_id(book_id)


def get_book_by_title_service(title):
    return Book.get_book_by_title(title)


def get_book_by_title_pattern_service(title_pattern):
    return Book.find_books_by_title_pattern(title_pattern)


def get_book_by_details_service(details):
    return Book.get_book_by_details(details)


def add_new_book(book):
    return Book.insert_book(book)


def del_book_by_id(book_id):
    return Book.delete_book_by_id(book_id)
