#! /usr/bin/python3.8
'''
In this example, we use the Schema Definition Language
to describe a simple table.
'''

from sqlalchemy import (create_engine, Table, Column, Integer, String, 
                        MetaData, inspect)

from . import Config

sqldb_addr: str = Config.sql_address()
sqldb_name: str = Config.sql_name()
sqldb_pass: str = Config.sql_pass()

eng = create_engine(
    f"mysql+pymysql://{sqldb_name}:{sqldb_pass}@{sqldb_addr}:3306/blog")


def table_represent():
    '''
    The MetaData is a container of a Table objects as well as
    an optional binding to an engine or connection. <-- What does this mean?

    Binding to an engine or connection?
    '''
    meta = MetaData()

    '''
    We create a metadata definition of a Cars table.
    The table has three columns, defined with the Column class.
    The datatypes of columns are defined with the Integer and String classes.
    '''
    cars = Table('Cars', meta,
                 Column('Id', Integer, primary_key=True),
                 Column('Name', String),
                 Column('Price', Integer),
                 )

    '''
    We access the Name column. The column are available thorugh the
    columns or c property.
    '''
    print("The Name column:")
    print(cars.columns.Name)
    print(cars.c.Name)  # A shortcut for above line.

    '''
    In this for loop, we print all the column names of the table.
    '''
    print("Columns")
    for col in cars.c:
        print(col)

    '''
    Printing primary keys of the table.
    '''
    print("Primary keys:")
    for pk in cars.primary_key:
        print(pk)

    print("The ID Column")
    print(cars.c.Id.name)
    print(cars.c.Id.type)
    print(cars.c.Id.nullable)
    print(cars.c.Id.primary_key)


def schema_reflect():

    meta = MetaData()
    meta.reflect(bind=eng)

    for table in meta.tables:
        print(table)


def schema_inspector():

    insp = inspect(eng)

    print(insp.get_table_names())
    print(insp.get_columns("Cars"))

    print(insp.get_pk_constraint("Cars"))
    print(insp.get_schema_names())
