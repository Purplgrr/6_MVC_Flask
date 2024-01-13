import sqlite3

connection = sqlite3.connect('library.sqlite')
cursor = connection.cursor()

with open('library.db', 'r', encoding ='utf-8-sig') as script_list:
    script = script_list.read()

cursor.executescript(script)
connection.commit()

connection.close()