import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel or creates from a dictionary"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime and saves to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
