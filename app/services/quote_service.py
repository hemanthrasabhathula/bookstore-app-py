from app.models.quote import Quote


def add_quote_service(quoteData, book_data):
    quote = {"quote": quoteData['quote'], "page": quoteData['page'], "chapter": quoteData['chapter'],
             "bookId": book_data['_id'], 'bookTitle': book_data['title']}
    return Quote.add_quote(quote)
