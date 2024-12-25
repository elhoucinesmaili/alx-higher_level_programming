#!/usr/bin/python3
"""Adds a new state and city to the database"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Establish connection to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)  # Create tables in the database

    # Set up session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add a new state to the database
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    # Create and add a new city to the database, linking it to the state
    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()

    # Close the session after operations are complete
    session.close()
