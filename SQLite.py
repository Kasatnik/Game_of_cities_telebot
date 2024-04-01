import sqlite3

db = sqlite3.connect("f.db")

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS kk (
    Username TEXT,
    points INTEGER,
    ID INTEGER NOT NULL
)""")

c.execute("INSERT INTO kk VALUES ('Roma', '22', 4545113)")

data = c.execute("SELECT Username FROM kk WHERE points < 100")
print(data.fetchall())
c.execute("UPDATE kk SET points = 12 WHERE points = 17")
c.execute("DELETE FROM kk WHERE points = 12")
db.commit()
