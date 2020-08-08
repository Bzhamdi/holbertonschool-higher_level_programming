#!/usr/bin/python3
"""
getAll matching
"""

from model_state import Base, State
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    match = session.query(City, State).join(State, State.id == City
                                            .state_id).order_by(City.id).all()
    for city in match:
        print("{}: ({}) {}".format(city.State.name, city.City.id,
                                   city.City.name))
    session.close()
