import sqlite3

conn = sqlite3.connect('qa.db')
cursor = conn.cursor()

cursor.execute("UPDATE Products SET price = price * 1.1 WHERE price < 10")
conn.commit()

conn.close()