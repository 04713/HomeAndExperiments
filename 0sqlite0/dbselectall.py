# -*- coding utf-8 -*-
import sqlite3, os

os.system('clear')

con = sqlite3.connect(r"/Users/dmitriyastahov/Documents/HOME_PROJEKTS/projPython/newdb.db")
cur = con.cursor() 

cur.execute("SELECT * FROM games")
print(cur.fetchall())

cur.close()
con.close()