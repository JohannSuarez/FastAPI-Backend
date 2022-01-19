#! /usr/bin/python

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship # What is sessionmaker?


'''
Documentation for Sessionmaker:
https://docs.sqlalchemy.org/en/13/orm/session_basics.html

In the most general sense, the Session establishes all conversations with the database
and represents a "holding zone" for all the objects which you've loaded or
associated with it during its lifespan. It provides the entrypoint to acquire a Query
object, which sends queries to the database using the Session object's current database
connection, populating result rows into objects that are then stored in the Session, inside
a structure called Identity Map - a data structure that maintains unique copies of each
object, where "unique" means "only one object with a particulata primary key".
'''



def orm_operations():

    eng = create_engine('sqlite:///:memory:')

    Base = declarative_base() # What is this?

    class Car(Base):
        __tablename__ = "Cars"

        Id = Column(Integer, primary_key=True)
        Name = Column(String)
        Price = Column(Integer)


    Base.metadata.bind = eng # What is this?
    Base.metadata.create_all() # What is this?

    Session = sessionmaker(bind=eng)
    ses = Session()

    '''
    The Session beings in an essentially stateless form.
    Once queries are issues or other objects are persisted with it
    it requests a connection resource from an Engine that is associated
    either with the Session itself or with the mapped Table objects being
    operated upon. This connection represents an ongoing transaction, which
    remains in effect until the Session is instructed to commit or roll back its
    pending state.
    '''

    '''
    When do I make a sessionmaker?

    Just one time, somewhere in your application's global scope.
    It should be looked upon as part of your application's configuration.

    If your application has three .py files in a package, you could,
    for example, place the sessionmaker line in your __init__.py file;

    from that point on your other modules say "from mypackage import Session".
    That way, everyone else just uses Session( ), and the configuration
    of that session is controlled by that central point.

    If your application starts up, does imports, but does not know what
    database it's going to be connection to, you can bind the 
    Session at the "class" level to the engine later on, 
    using sessionmaker.configure()

    In the examples shown, we will frequently show the sessionmaker
    being created right above the line where we invoke Session.
    In reality, the sessionmaker would be somewhere at the module
    level. The calls to instantiate Session would then be placed at the
    point in the application where database conversations begin.

    TDLR:
    As a general rule, keep the lifecycle of the session separate and external
    from functions and objects that access and/or manipulate database data.
    This will greatly help with achieving a predictable and consistent
    transactional scope.
    
    Make sure you have a clear notion of where transactons begin and
    end, and keep transactions short, meaning, they end
    at the series of a sequence of operations, instead of 
    being held open indefinitely.

    '''

    ses.add_all(
            [Car(Id=1, Name='Audi', Price=52642),
             Car(Id=2, Name='Mercedes', Price=57127),
             Car(Id=3, Name='Skoda', Price=9000),
             Car(Id=4, Name='Volvo', Price=29000),
             Car(Id=5, Name='Bentley', Price=350000),
             Car(Id=6, Name='Citroen', Price=21000),
             Car(Id=7, Name='Hummer', Price=41400),
             Car(Id=8, Name='Volkswagen', Price=21600)])

    '''
    All changes to objects maintained by a Session are tracked - before
    the database is queried again or before the current transaction is committed,
    it flushes all pending changes to the database. This is known as the Unit of Work 
    pattern.
    '''

    ses.commit() # What is this?

    rs = ses.query(Car).all()

    for car in rs:
        print(f'{car.Name}, {car.Price}')

    # Adding to the Database
    print("--- Adding a New Car ---")
    c1 = Car(Name='Oldsmobile', Price=23450)
    ses.add(c1)
    ses.commit()

    rs = ses.query(Car).all()

    for car in rs:
        print(f'{car.Name}, {car.Price}')

    # Querying for a car with a name that ends in "en"
    print("---Testing query operations---")

    rs = ses.query(Car).filter(Car.Name.like('%en'))

    for car in rs:
        print(f'{car.Name}, {car.Price}')


def orm_foreign_key():

    eng = create_engine('sqlite:///alch_practice/author_books.db')
    Base = declarative_base() # What is this?

    class Author(Base):
        __tablename__ = "Authors"
        AuthorId = Column(Integer, primary_key=True)
        Name = Column(String)
        Books = relationship("Book")

    class Book(Base):
        __tablename__ = "Books"
        BookId = Column(Integer, primary_key=True)
        Title = Column(String)
        AuthorId = Column(Integer, ForeignKey("Authors.AuthorId"))
        Author = relationship("Author")


    Session = sessionmaker(bind=eng)
    ses = Session()

    res = ses.query(Author).filter(Author.Name=="Leo Tolstoy").first()

    for book in res.Books:
        print(book.Title)

    res = ses.query(Book).filter(Book.Title=="Emma").first()
    print(res.Author.Name)
