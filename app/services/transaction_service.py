from app.models.transaction import Transaction


def get_all_transactions():
    return Transaction.get_all_transactions()


def get_all_user_transactions(user_id):
    return Transaction.get_all_user_transactions(user_id)


def add_transactions(transactions):
    return Transaction.add_transactions(transactions)
