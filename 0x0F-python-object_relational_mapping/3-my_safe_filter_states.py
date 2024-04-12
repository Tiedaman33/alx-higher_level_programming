#!/usr/bin/python3

import MYSQLdb
import sys

if __name__ =="__main__":
    db = MYSQL.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    match = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
