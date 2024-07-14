from app.models.book import Book


def get_books():
    return Book.get_all_books()


def get_book_by_id(book_id):
    return Book.get_book_by_id(book_id)


def add_new_book(book):
    return Book.insert_book(book)


def del_book_by_id(book_id):
    return Book.delete_book_by_id(book_id)
