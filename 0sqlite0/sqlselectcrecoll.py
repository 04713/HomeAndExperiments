# -*- coding utf-8 -*-
import sqlite3

def myfunc(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:", isolation_level=None)
con.create_collation("myfunc", myfunc)
cur = con.cursor()
cur.execute("CREATE TABLE games (name TEXT)")
cur.execute("INSERT INTO games VALUES ('blood1')")
cur.execute("INSERT INTO games VALUES ('Bloodlu')")
cur.execute("INSERT INTO games VALUES ('Blood2')")

# standart sort
cur.execute("SELECT * FROM games ORDER BY name")
for i in cur:
    print(i)

print('*' * 13)

# user sort
cur.execute("""SELECT * FROM games ORDER BY name COLLATE myfunc""")
for i in cur:
    print(i)

cur.close()
con.close()
