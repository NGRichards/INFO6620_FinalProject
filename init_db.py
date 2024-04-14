import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO student (StudentName, StudentEmail) VALUES (?, ?)", ('Test Student', 'Test.Student@dal.ca'))
cur.execute("INSERT INTO prompts (StudentID, Style, Reference, Msg) VALUES (?, ?, ?, ?)", (1, 'Test APA', 'This is my test form. It is great!', 'This is a test response. It is not as great as you thought.'))


connection.commit()
connection.close()