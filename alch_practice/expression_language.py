from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer
from sqlalchemy.sql import select, and_, asc, tuple_

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


def where_method():
    '''
    This example uses .where
    to select all cars whose price is
    between 10000 and 40000
    '''

    with eng.connect() as con:

        meta = MetaData(eng)
        cars = Table('Cars', meta, autoload=True)

        stm = select([cars]).where(and_(cars.c.Price > 10000),
                                   (cars.c.Price < 40000))

        rs = con.execute(stm)
        print(rs.fetchall())


def like_method():

    with eng.connect() as con:
        meta = MetaData(eng)
        cars = Table('Cars', meta, autoload=True)
        stm = select([cars]).where(cars.c.Name.like('%en'))

        rs = con.execute(stm)

        print(rs.fetchall())


def select_order():

    with eng.connect() as con:
        metadata = MetaData(eng)
        cars = Table('Cars', metadata, autoload=True)

        s = select([cars]).order_by(asc(cars.c.Name))
        rs = con.execute(s)

        for row in rs:
            print(f"{row['Id']}, {row['Name']}, {row['Price']}")


def select_in():

    with eng.connect() as con:
        meta = MetaData(eng)
        cars = Table('Cars', meta, autoload=True)

        k = [(2,), (4,), (6,), (8,)]
        stm = select([cars]).where(tuple_(cars.c.Id).in_(k))
        rs = con.execute(stm)

    for row in rs:
        print(f"{row['Id']}, {row['Name']}, {row['Price']}")


def create_table():

    eng = create_engine('sqlite:///:memory:')

    with eng.connect() as con:
        meta = MetaData(eng)
        cars = Table('Cars', meta,
                     Column('Id', Integer, primary_key=True),
                     Column('Name', String),
                     Column('Price', Integer)
                     )

        cars.create()

        ins1 = cars.insert().values(Id=1, Name='Audi', Price=52642)
        con.execute(ins1)

        ins2 = cars.insert().values(Id=2, Name='Mercedes', Price=57127)
        con.execute(ins2)

        ins3 = cars.insert().values(Id=3, Name='Skoda', Price=6000)
        con.execute(ins3)

        s = select([cars])
        rs = con.execute(s)

        for row in rs:
            print(f"{row['Id']}, {row['Name']}, {row['Price']}")


def join_tables():

    eng = create_engine('sqlite:///test.db')

    with eng.connect() as con:
        meta = MetaData(eng)

        authors = Table('Authors', meta, autoload=True)
        books = Table('Books', meta, autoload=True)

        stm = select([authors.join(books)])
        rs = con.execute(stm)

        for row in rs:
            print(f"{row['Name']}, {row['Title']}")
