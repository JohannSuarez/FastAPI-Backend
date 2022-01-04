#! /usr/bin/python3.8
# -*- coding: utf-8 -*-

"""
Source: https://zetcode.com/db/sqlalchemy/rawsql/
"""

from . import Config
from sqlalchemy import create_engine, text


# Originally raw_create_table.py
def create_table():

    sqldb_name: str = Config.sql_name()
    sqldb_addr: str = Config.sql_address()
    sqldb_pass: str = Config.sql_pass()

    eng = create_engine(
        f"mysql+pymysql://{sqldb_name}:{sqldb_pass}@{sqldb_addr}:3306/blog")

    with eng.connect() as con:

        con.execute(text('DROP TABLE IF EXISTS Cars'))
        con.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY,
            Name TEXT, Price INTEGER)'''))

        data = ({"Id": 1, "Name": "Audi", "Price": 52642},
                {"Id": 2, "Name": "Mercedes", "Price": 57127},
                {"Id": 3, "Name": "Skoda", "Price": 9000},
                {"Id": 4, "Name": "Volvo", "Price": 29000},
                {"Id": 5, "Name": "Bentley", "Price": 350000},
                {"Id": 6, "Name": "Citroen", "Price": 21000},
                {"Id": 7, "Name": "Hummer", "Price": 41400},
                {"Id": 8, "Name": "Volkswagen", "Price": 21600}
                )

        for line in data:
            con.execute(text("""INSERT INTO Cars(Id, Name, Price)
                VALUES(:Id, :Name, :Price)"""), **line)


# Originally raw_column_names.py
def read_column_names():


    sqldb_name: str = Config.sql_name()
    sqldb_addr: str = Config.sql_address()
    sqldb_pass: str = Config.sql_pass()

    eng = create_engine(
        f"mysql+pymysql://{sqldb_name}:{sqldb_pass}@{sqldb_addr}:3306/blog")

    with eng.connect() as con:
        # con.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY,
        #     Name TEXT, Price INTEGER)'''))

        rs = con.execute(text('SELECT * FROM Cars'))

        print(rs.keys())
