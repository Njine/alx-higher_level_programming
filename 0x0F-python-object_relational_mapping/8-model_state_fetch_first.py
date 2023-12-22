#!/usr/bin/python3
"""
Script that retrieves and prints the first State object from a database using SQLAlchemy.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Create a SQLAlchemy engine for connecting to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first State object from the database
    first_state = session.query(State).first()

    # Check if there are any states in the database
    if not first_state:
        print("Nothing")
    else:
        # Print the information of the first State object
        print("{}: {}".format(first_state.id, first_state.name))
