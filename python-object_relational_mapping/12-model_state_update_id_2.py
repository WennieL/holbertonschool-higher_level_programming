#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    usrname = argv[1]
    pwd = argv[2]
    db_name = argv[3]

    connect_str = f"mysql+mysqldb://{usrname}:{pwd}@localhost:3306/{db_name}"

    engine = create_engine(connect_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    update_state = session.query(State).filter(State.id == 2).first()

    if update_state:
        update_state.name = "New Mexico"
        session.commit()

    session.close()
