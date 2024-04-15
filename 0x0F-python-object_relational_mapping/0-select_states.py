#!/usr/bin/python3
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "hbtn_0e_0_usa"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
