from app.models.transaction import Transaction


def get_all_transactions():
    return Transaction.get_all_transactions()


def get_all_user_transactions(user_id):
    return Transaction.get_all_user_transactions(user_id)


def get_copy_transactions(copy_id):
    return Transaction.get_copy_transactions(copy_id)


def get_copy_transactions_by_status(copy_id, status):
    return Transaction.get_copy_transactions_by_status(copy_id, status)


def add_transactions(transactions):
    return Transaction.add_transactions(transactions)


def update_transaction(transaction_id, data):
    return Transaction.update_transaction(transaction_id, data)
