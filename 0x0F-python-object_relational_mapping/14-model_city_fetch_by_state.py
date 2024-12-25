#!/usr/bin/python3
"""List all cities and their respective states"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    
    # Create all tables if they don't exist
    Base.metadata.create_all(engine)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for cities and their related state names
    cities = session.query(City, State).filter(City.state_id == State.id).all()
    
    # Display each city and its corresponding state in the required format
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    # Commit the session and close it
    session.commit()
    session.close()
