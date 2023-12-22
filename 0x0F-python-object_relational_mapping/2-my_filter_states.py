#!/usr/bin/python3
"""Displays all states from the database hbtn_0e_0_usa matching the provided name"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Get MySQL username, password, database name, and state name from command line arguments
    username, password, dbname, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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
        # Execute the SQL query to select states matching the provided name
        cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '%{}%'\
            ORDER BY states.id ASC".format(state_name))
        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Iterate over the rows and print each one
        for row in rows:
            print(row)

    # Close the cursor and database connection
    db.close()
