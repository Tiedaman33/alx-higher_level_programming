#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.

Returns:
    None

Requirements:
    - The script should import MySQLdb.
    - It should connect to a MySQL server running on localhost at port 3306.
    - Results must be sorted in ascending order by cities.id.
    - Only one call to execute() should be used.
    - Results must be displayed as they are in the example below.
    - The code should not be executed when imported.

Example:
    If the script is executed as follows:

    $ python script.py myuser mypassword hbtn_0e_4_usa

    Output:
    (1, 'New York')
    (2, 'San Francisco')
    ...
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
    c.execute("""SELECT cities.id, cities.name, states.name FROM cities
              INNER JOIN states ON states.id=cities.state.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
