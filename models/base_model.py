#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel defines all common attributes/methods for other classes.
    
    Attributes:
        id (str): Unique identifier for each instance, assigned with a UUID.
        created_at (datetime): The date and time when the instance is created.
        updated_at (datetime): The date and time when the instance is last updated.
    """

    def __init__(self):
        """Initializes a new BaseModel instance with a unique id and current timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dict_repr = self.__dict__.copy()  # Copy the instance dictionary
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()  # Convert to ISO format
        dict_repr["updated_at"] = self.updated_at.isoformat()  # Convert to ISO format
        return dict_repr
