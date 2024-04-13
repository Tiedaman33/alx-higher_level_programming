#!/usr/bin/python3

"""
Write a script that lists all states from the database hbtn_0e_0_usa.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.

Returns:
    None

Requirements:
    - The script should import MySQLdb.
    - It should connect to a MySQL server running on localhost at port 3306.
    - Results must be sorted in ascending order by states.id.
    - Results must be displayed as they are in the example below.
    - The code should not be executed when imported.

Example:
    If the script is executed as follows:

    $ python script.py myuser mypassword hbtn_0e_0_usa

    Output:
    (1, 'Alabama')
    (2, 'Alaska')
    (3, 'Arizona')
    ...
"""

import MySQLdb
import sys

if __nam__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2],  db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
