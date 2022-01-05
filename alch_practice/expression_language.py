from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select

from . import Config

sqldb_addr: str = Config.sql_address()
sqldb_name: str = Config.sql_name()
sqldb_pass: str = Config.sql_pass()

eng = create_engine(
    f"mysql+pymysql://{sqldb_name}:{sqldb_pass}@{sqldb_addr}:3306/blog")


def select_all():

    with eng.connect() as con:

        meta = MetaData(eng)
        cars = Table('Cars', meta, autoload=True)

        stm = select([cars])
        rs = con.execute(stm)

        print(rs.fetchall())


def select_limited():

    with eng.connect() as con:
        meta = MetaData(eng)
        cars = Table('Cars', meta, autoload=True)

        stm = select([cars.c.Name, cars.c.Price]).limit(3)
        rs = con.execute(stm)

        print(rs.fetchall())
