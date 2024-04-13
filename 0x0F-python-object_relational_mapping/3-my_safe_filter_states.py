#!/usr/bin/python3

"""
Write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument in a safe manner,
preventing SQL injection attacks.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.
    state_name (str): The state name to search for in the states table.

Returns:
    None

Requirements:
    - The script should import MySQLdb.
    - It should connect to a MySQL server running on
    localhost at port 3306.
    - Results must be sorted in ascending order by states.id.
    - Results must be displayed as they are in the example below.
    - The code should not be executed when imported.

Example:
    If the script is executed as follows:

    $ python script.py myuser mypassword hbtn_0e_0_usa "New York"

    Output:
    (4, 'New York')
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    c = db.cursor()
    match = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
