#!/usr/bin/python3

import MYSQLdb
import sys

if __name__ =="__main__":
    db = MYSQL.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WhERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
