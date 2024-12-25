#!/usr/bin/python3
"""
Module that lists all states from the hbtn_0e_0_usa database where name matches the argument.
This script is safe from SQL injection.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC;"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and print all matching rows
    results = cursor.fetchall()
    for state in results:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
