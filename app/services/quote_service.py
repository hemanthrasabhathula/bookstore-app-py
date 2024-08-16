from app.models.quote import Quote


def add_quote_service(quoteData, currentBook):
    quote = {"quote": quoteData['quote'], "page": quoteData['page'], "chapter": quoteData['chapter'],
             "bookId": currentBook['_id'], 'bookTitle': currentBook['title']}
    return Quote.add_quote(quote)
