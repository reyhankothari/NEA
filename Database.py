import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
DROP TABLE ProductInformation""")

conn.commit()
conn.close()