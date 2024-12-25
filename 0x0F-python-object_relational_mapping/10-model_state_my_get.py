#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    # Set up the connection to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with the name passed as an argument
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display the results
    if state:
        print(state.id)
    else:
        print("Not found")
