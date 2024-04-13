#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Args:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): Name of the database.
    state_name (str): The state name to search for in the states table.

Returns:
    None

Requirements:
    - The script should import MySQLdb.
    - It should connect to a MySQL server running on localhost at port 3306.
    - The SQL query should be formatted using
    the user input for the state name.
    - Results must be sorted in ascending order by states.id.
    - Results must be displayed as they are in the example below.
    - The code should not be executed when imported.

Example:
    If the script is executed as follows:

    $ python script.py myuser mypassword hbtn_0e_0_usa California

    Output:
    (5, 'California')
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
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
              .format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
