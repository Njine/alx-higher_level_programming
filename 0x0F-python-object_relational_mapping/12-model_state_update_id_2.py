#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database.
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

        new_instance = session.query(State).filter_by(id=2).first()
        if new_instance:
            new_instance.name = 'New Mexico'
            session.commit()
        else:
            print("State with id=2 not found.")

    except Exception as e:
        print("Error: {}".format(e))

    finally:
        session.close()
