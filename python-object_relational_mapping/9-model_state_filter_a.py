#!/usr/bin/python3
"""
    show elements in database with alchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    con = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(con.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    statesList = session.query(State).where(State.name.like('%a%'))

    for i, j in enumerate(statesList, 1):
        print(f"{i}: {j.name}")
