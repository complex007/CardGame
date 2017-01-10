#!/usr/bin/env python
import sqlite3
conn = sqlite3.connect("doudizhu.db")

c = conn.cursor()

# create tables
c.execute('''create TABLE player
      (id INTEGER PRIMARY  KEY, name text, wealth int, avatar text)''')
# c.execute('DROP TABLE book')
# save the changes
conn.commit()

# close the connection with the database
conn.close()
