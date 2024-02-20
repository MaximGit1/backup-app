import sqlite3

db = sqlite3.connect('data.db')
sql = db.cursor()
count = sql.execute("Select count(*) from history").fetchall()[0][0]
rows = sql.execute("Select * from history").fetchall()
