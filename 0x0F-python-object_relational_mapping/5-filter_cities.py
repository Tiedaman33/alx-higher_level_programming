#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.
    state_name (str): The name of the state to list
    cities for (SQL injection free).

Returns:
    None

Requirements:
    - The script should import MySQLdb.
    - It should connect to a MySQL server running on localhost at port 3306.
    - Results must be sorted in ascending order by cities.id.
    - Only one call to execute() should be used.
    - The results must be displayed as they are in the example below.
    - The code should not be executed when imported.

Example:
    If the script is executed as follows:

    $ python script.py myuser mypassword hbtn_0e_4_usa "California"

    Output:
    (5, 'San Francisco')
    (6, 'Los Angeles')
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
    c.execute("""SELECT cities.name
              FROM CITIES INNER JOIN states ON states.id=cities.state_id
              WHERE states.name=%s""", (sys.argv[4],))
    rows = c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    c.close()
    db.close()
