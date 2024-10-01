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

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance with a unique id and current timestamps or from kwargs."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        # Convert string to datetime object
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
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

if __name__ == "__main__":
    # Create an instance of BaseModel
    instance = BaseModel()
    
    # Print the string representation of the instance
    print(instance)
    
    # Save the instance to update the updated_at attribute
    instance.save()
    
    # Print the updated instance
    print(instance)
    
    # Convert the instance to a dictionary and print it
    instance_dict = instance.to_dict()
    print(instance_dict)
