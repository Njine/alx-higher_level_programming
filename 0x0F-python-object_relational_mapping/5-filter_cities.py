#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    # Get MySQL username, password, database name, and state name from command line arguments
    username, password, dbname, state_name = sys.argv[1:5]

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
        # Execute the SQL query to select cities of the given state
        cursor.execute("""
            SELECT cities.name
            FROM cities
            LEFT JOIN states ON states.id = cities.state_id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id ASC
        """, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Extract city names and join them into a comma-separated string
        city_names = ", ".join(row[0] for row in rows)
        print(city_names)

    # Close the cursor and database connection
    db.close()
