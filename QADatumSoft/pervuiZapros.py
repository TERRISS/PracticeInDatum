import sqlite3

conn = sqlite3.connect('qa.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM Users WHERE age > 30")

results = cursor.fetchall()

for row in results:
    print(row[0])

conn.close()

