# AirBnB Clone - Command Interpreter

This is the first step toward creating a full web application like AirBnB. This command interpreter manages the backend of the project by handling operations like object creation, updating, deletion, and serialization.

## Features
- Create objects like `User`, `Place`, `City`, `Amenity`, `Review`, and more.
- View objects.
- Update attributes of objects.
- Delete objects.
- Save object data to a file.

## How to Start
Run the command interpreter:
```bash
./console.py

Output Examples:

1. # Creating a new instance of BaseModel
new_instance = BaseModel()
print(new_instance)

Output: [BaseModel] (d2e3b0bc-4f5d-4f4e-9fcb-733a8e9e0e7d) {'id': 'd2e3b0bc-4f5d-4f4e-9fcb-733a8e9e0e7d', 
'created_at': datetime.datetime(2024, 10, 2, 10, 15, 30), 'updated_at': datetime.datetime(2024, 10, 2, 10, 15, 30)}

2. # Creating a new instance of BaseModel with attributes
new_instance = BaseModel(name="Example", age=30)
print(new_instance)

Output: [BaseModel] (e3b3e4fc-12a4-4d56-87ba-cd3b5a7e6d8e) {'id': 'e3b3e4fc-12a4-4d56-87ba-cd3b5a7e6d8e', 
'created_at': datetime.datetime(2024, 10, 2, 10, 15, 35), 'updated_at': datetime.datetime(2024, 10, 2, 10, 15, 35), 'name': 'Example', 'age': 30}

3. # Creating and saving a new instance
new_instance = BaseModel()
new_instance.name = "Test"
new_instance.save()
print(new_instance)

Output: [BaseModel] (b1c1e3fc-12a4-4d56-87ba-cd3b5a7e6d8f) {'id': 'b1c1e3fc-12a4-4d56-87ba-cd3b5a7e6d8f', 
'created_at': datetime.datetime(2024, 10, 2, 10, 15, 40), 'updated_at': datetime.datetime(2024, 10, 2, 10, 15, 45), 'name': 'Test'}
