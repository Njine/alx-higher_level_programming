#!/usr/bin/python3
"""
Script that retrieves and lists all State objects from a database.
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

    # Create tables based on the defined models (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects and print the results in ascending order by ID
    for state_id, state_name in session.query(State.id, State.name).order_by(State.id):
        print("{}: {}".format(state_id, state_name))
