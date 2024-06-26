from datetime import datetime
from sqlalchemy import inspect
from sqlalchemy.orm import validates

from . import db



class Order(db.Model):
    '''
    Order: basic ORM class representing the structure of the database. Built based on SQLALchemy's db.Model base class.

    Fields:
    - id - automatically generated incrementing integer. Primary key of the table. Used to refer to each 
    - creation_date - DateTime object. Automatically generated during the creation of an entry, uses the server's current time.
    - status - short string with only three valid values: "New", "In progress", and "Completed". Any value outside of that will result in a ValueError.

    - name - User provided string with up to 100 chars. The name of an order. 
    - description - User provided string with up to 300 chars.

    Methods:
    - __repr__ - representation string. Applies when the Order object is called by itself.
    - toDict - converts the object's values into a dictionary representation. Useful for further interactions with SQLAlchemy.
    '''

    __tablename__ = "orders"

    # Automatically created/managed fields
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    creation_date = db.Column(db.DateTime(timezone=True), default=datetime.now)
    status = db.Column(db.String(50), nullable=False)

    # User provided fields
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable = True)

    def __repr__(self) -> str:
        return f'Order: {self.name} with id {self.id}.'
        
    def toDict(self) -> dict:
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
    

    @validates('status')
    def validate_status(self, key, value):
        valid_status_names = ["New", "In progress", "Completed"]

        if value not in valid_status_names:
            raise ValueError(f"Given value '{value}' is not a valid status.")
        
        return value