'''
Services are defined in the services package. Each service
is a subclass of AppService. The database session is passed down
from the request dependency via an "interface-like" mixin utility class
(other mixin classes may be added via multiple inheritance in order to
extend available attributes)
'''

from sqlalchemy.orm import Session

class DBSessionMixin:
    def __init__(self, db: Session):
        self.db = db

class AppService(DBSessionMixin):
    pass

class AppCRUD(DBSessionMixin):
    pass
