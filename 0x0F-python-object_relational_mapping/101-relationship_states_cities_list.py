#!/usr/bin/python3
"""
post
"""

from relationship_state import Base, State
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for st in states:
        print("{}: {}".format(st.id, st.name))
        for c in st.cities:
            print("\t", c.id, ': ', c.name)
    session.close()
