#!/usr/bin/python3
"""List all states and their cities"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating the engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get all states and their associated cities
    states = session.query(State).order_by(State.id).all()
    
    # Iterate over each state and its cities
    for state in states:
        print(f"{state.id}: {state.name}")
        # Print each city related to the state
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session after use
    session.close()
