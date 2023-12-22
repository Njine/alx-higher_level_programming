#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    try:
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for instance in session.query(State).filter(State.name.like('%a%')):
            session.delete(instance)
        session.commit()

    except Exception as e:
        print("Error: {}".format(e))

    finally:
        session.close()
