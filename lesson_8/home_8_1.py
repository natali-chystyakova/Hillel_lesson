import os
import sqlite3


db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()

# Вариант 1
query_sql = '''
  SELECT SUM(UnitPrice * Quantity)
    FROM invoice_items;
'''

rows = cur.execute(query_sql).fetchall()
print(rows)
for row in rows:
    print(*row)

# Вариант 2
query_sql1 = '''
  SELECT UnitPrice, Quantity
    FROM invoice_items; 
'''

rows = cur.execute(query_sql1).fetchall()
print(*rows)
l = []
for row in rows:
    l.append(row[0] * row[1])
print(l)
result = sum(l)
print(result)

connection.close()















