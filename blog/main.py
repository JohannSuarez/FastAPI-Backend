from blog import Config
from blog import db
from blog import sqlalchem
from typing import Union


def connect() -> Union[None, list]:
    """
    Interact with Database wrapper,
        attempt to connect to database.
    """

    dn = db.DBInterface(Config.sql_address(),
                        Config.sql_name(),
                        Config.sql_pass(),
                        Config.sql_db(),
                        Config.sql_table())


    #res = dn.fetch_tables()
    res = dn.list_table_data() or "No results"

    print(res)
    return(res)

def sql_alch() -> None:
    sqlalchem.sql_alch_test()

def drive() -> None:
    print("Test function.")


if __name__ == "__main__":
    drive()
