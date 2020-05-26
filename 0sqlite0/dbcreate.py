# -*- coding utf-8 -*-
import sqlite3

con = sqlite3.connect(r"/Users/dmitriyastahov/Documents/GIT_PROJEKTS/0sqlite0/newdb.db")
cur = con.cursor()
cur.execute('CREATE TABLE games (ID int, Name varchar(100), Country varchar(100))')
cur.execute('INSERT INTO games VALUES (0, "pong", "USA")')
con.commit()

cur.close()
con.close()