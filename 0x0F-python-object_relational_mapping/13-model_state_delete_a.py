#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a' from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Set up the connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all states containing the letter 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete all those states
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()
