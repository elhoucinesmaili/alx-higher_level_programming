#!/usr/bin/python3
"""
Lists all cities of a state from the database.
"""

import MySQLdb
import sys

def list_cities_by_state(user, password, db_name, state_name):
    """Connects to the database and lists cities of the given state."""
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

        # Create a cursor to execute the query
        with connection.cursor() as cursor:
            # Execute the parameterized query
            query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;
            """
            cursor.execute(query, (state_name,))

            # Fetch and format the result
            cities = [city[0] for city in cursor.fetchall()]
            print(", ".join(cities))
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Ensure connection is closed
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: ./<script_name>.py <mysql_user> <mysql_password> <db_name> <state_name>")
