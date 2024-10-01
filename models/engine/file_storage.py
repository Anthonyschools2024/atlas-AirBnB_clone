import json
import os

class FileStorage:
    """Class that serializes and deserializes instances to and from a JSON file."""
    
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to a JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    # You can add more classes here as needed
