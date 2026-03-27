import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT, name TEXT)")

cursor.execute("INSERT INTO students VALUES(1,'Yash')")

conn.commit()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()