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
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
