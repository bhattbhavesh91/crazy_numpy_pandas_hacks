#!/usr/bin/env python3


import sqlite3
import re

# find your 'History' file
conn = sqlite3.connect('c:/Users/Bhavesh/AppData/Local/Google/Chrome/User Data/Default/History')
c = conn.cursor()

result = True
id = 0
while result:
    result = False
    ids = []
    for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%github%'"""):
        print (row)
        id = row[0]
        ids.append((id,))
    c.executemany('DELETE FROM urls WHERE id=?', ids)
    conn.commit()

conn.close()