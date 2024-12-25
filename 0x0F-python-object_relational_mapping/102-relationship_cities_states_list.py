#!/usr/bin/python3
"""List all cities and states"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the database engine using command-line arguments for login credentials
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and states, joining the two tables on the state_id field
    for city, state in session.query(City, State).\
                        join(State, State.id == City.state_id).\
                        order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    # Close the session
    session.close()

