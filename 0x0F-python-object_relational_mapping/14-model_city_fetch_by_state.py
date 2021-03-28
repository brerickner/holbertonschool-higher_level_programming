#!/usr/bin/python3
'''Module  Python file similar to model_state.py named model_city.py
that contains the class definition of a City.'''

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    vroom = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(argv[1], argv[2], argv[3])
    engine = create_engine(vroom)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).join(State)\
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
