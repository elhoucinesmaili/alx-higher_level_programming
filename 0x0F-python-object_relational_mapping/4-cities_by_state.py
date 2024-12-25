#!/usr/bin/python3
"""
Lists all cities from the database along with their state names.
"""

import MySQLdb
import sys

def list_cities(user, password, db_name):
    """Connects to the MySQL database and retrieves cities and their states."""
    try:
        # Connect to the database
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor to execute queries
        with connection.cursor() as cursor:
            # Execute the query
            query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
            """
            cursor.execute(query)

            # Fetch and print each row of the result
            for row in cursor.fetchall():
                print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Ensure connection is closed
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./<script_name>.py <mysql_user> <mysql_password> <db_name>")
