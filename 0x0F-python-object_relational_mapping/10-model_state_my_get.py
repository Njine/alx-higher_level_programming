#!/usr/bin/python3
"""
Script that retrieves and prints the ID of a State object
based on the provided state name from a database using SQLAlchemy.
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

    # Query the State object based on the provided state name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the state ID or "Not found" if the state doesn't exist
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
