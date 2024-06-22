#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    usrname = argv[1]
    pwd = argv[2]
    db_name = argv[3]
    connect_str = f"mysql+mysqldb://{usrname}:{pwd}@localhost:3306/{db_name}"

    engine = create_engine(connect_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
