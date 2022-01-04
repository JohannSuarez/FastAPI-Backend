from . import Config
from sqlalchemy import create_engine, text


def sql_alch_test():
    sqldb_name: str = Config.sql_name()
    sqldb_addr: str = Config.sql_address()
    sqldb_pass: str = Config.sql_pass()

    engine = create_engine(f"mysql+pymysql://{sqldb_name}:{sqldb_pass}@{sqldb_addr}:3306");

    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())



#def sql_alch_test():
#    print("FCCK")
