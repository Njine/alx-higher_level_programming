#!/usr/bin/python3
"""
Script that lists all State objects from a database
where the name contains the letter 'a'.
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

    # Query and print State objects where the name contains the letter 'a'
    for state in session.query(State).filter(State.name.contains('%a')).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
