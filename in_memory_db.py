class TransactionError(Exception):
    pass

class InMemoryDB:
    def __init__(self):
        self.data = {}               
        self.transaction_data = {}   
        self.in_transaction = False

    def begin_transaction(self):
        if self.in_transaction:
            raise TransactionError("Transaction already in progress")
        self.in_transaction = True
        self.transaction_data = {}

    def put(self, key, val):
        if not self.in_transaction:
            raise TransactionError("No active transaction")
        self.transaction_data[key] = val

    def get(self, key):
        if self.in_transaction and key in self.transaction_data:
            return None  
        return self.data.get(key)

    def commit(self):
        if not self.in_transaction:
            raise TransactionError("No active transaction")
        self.data.update(self.transaction_data)
        self.transaction_data = {}
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise TransactionError("No active transaction")
        self.transaction_data = {}
        self.in_transaction = False
