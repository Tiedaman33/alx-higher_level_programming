#!/usr/bin/python3

"""
script that lists all states from the database hbtn_0e_0_usa
arguments:
    mysql username
    mysql password
    database name
connects to mysql on local host at port 3306
"""

import MySQLdb
import sys

if __name == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2],  db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        pront(row)
    c.close()
    db.close()
