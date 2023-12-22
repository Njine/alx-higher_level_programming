#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get MySQL username, password, and database name from command line arguments
    username, password, dbname = sys.argv[1:4]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    # Create a cursor object to interact with the database
    with db.cursor() as cursor:
        # Execute the SQL query to select cities with corresponding state names
        cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC
        """)

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Iterate over the rows and print each one
        for row in rows:
            print(row)

    # Close the cursor and database connection
    db.close()
