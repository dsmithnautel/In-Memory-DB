from in_memory_db import InMemoryDB, TransactionError

db = InMemoryDB()

print(db.get("A"))         # None
try:
    db.put("A", 5)
except TransactionError as e:
    print(e)               # No active transaction

db.begin_transaction()
db.put("A", 5)
print(db.get("A"))         # None
db.put("A", 6)
db.commit()
print(db.get("A"))         # 6

try:
    db.commit()
except TransactionError as e:
    print(e)               # No active transaction

try:
    db.rollback()
except TransactionError as e:
    print(e)               # No active transaction

print(db.get("B"))         # None
db.begin_transaction()
db.put("B", 10)
db.rollback()
print(db.get("B"))         # None
