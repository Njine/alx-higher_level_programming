#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Get MySQL username, password, database name, and state name from command line arguments
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

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
        # Execute the SQL query to select states matching the provided name (using parameters)
        cursor.execute("SELECT * FROM states WHERE name = (%s)\
            ORDER BY states.id ASC", (state_name,))
        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Iterate over the rows and print each one
        for row in rows:
            print(row)

    # Close the cursor and database connection
    db.close()
