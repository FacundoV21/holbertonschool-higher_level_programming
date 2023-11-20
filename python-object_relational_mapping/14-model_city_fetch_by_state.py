#!/usr/bin/python3
"""
    show elements in database with alchemy
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    con = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(con.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(City, State)
    st = st.join(State, State.id == City.state_id).all()

    for city, state in st:
        print(f"{state.name}: ({city.id}) {city.name}")
