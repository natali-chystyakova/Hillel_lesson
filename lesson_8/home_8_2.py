import os
import sqlite3

# Устанавлием соединение с БД
db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)
cur = connection.cursor()


query_sql = '''
     SELECT FirstName, COUNT (FirstName)
       FROM customers GROUP BY FirstName;
'''
rows = cur.execute(query_sql).fetchall()

print(rows)
for row in rows:
    if row[1] > 1:
        print(row)


connection.close()



