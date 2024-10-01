#!/usr/bin/python3
from models.base_model import BaseModel

if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model)               # This should print the object in the correct format
    print(type(my_model))         # This should print: <class 'models.base_model.BaseModel'>
    print(isinstance(my_model, BaseModel))  # This should print: True
