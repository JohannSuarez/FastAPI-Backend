from os.path import join, dirname
from dotenv import load_dotenv
from typing import Union, Any

import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection, CMySQLCursor

'''
    Class that wraps around mysql.connector.
    The interface has all the methods
    needed to fetch data from the databse.
'''

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class DBInterface():

    def __init__(self, db_address: str, 
                       db_username: str,
                       db_password: str,
                       db_name: str,
                       db_table: str
                       ) -> None:

        self._db_address: str = db_address # IP Address
        self._db_username: str = db_username # User's Name
        self._db_password: str = db_password
        self._db_name: str = db_name # Name of the database in the server.
        self._db_table: str = db_table # The table within the database.
        self._connection: Union[None, CMySQLConnection] = None
        self._cursor: Union[None, CMySQLCursor] = None

        self._connect_db()
        
    def _connect_db(self) -> None:
        self.connection = mysql.connector.connect(
            host=self._db_address,
            user=self._db_username,
            password=self._db_password
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"USE {self._db_name}") 


    def fetch_tables(self) -> Union[list, None]:
        if self.cursor:
            self.cursor.execute("SHOW DATABASES")
            return self.cursor.fetchall() 

    def list_table_data(self) -> Any:   
        if self.cursor:
            try:
                self.cursor.execute(f"SELECT * FROM {self._db_table}")
                return self.cursor.fetchall() 
            except Exception as error:
                print(f"Caught Exception in db.py's list_table_data - {error}")

            #return ( self.cursor.fetchall() )
            
