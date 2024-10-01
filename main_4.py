#!/usr/bin/python3
from models.base_model import BaseModel

if __name__ == "__main__":
    my_model = BaseModel()
    print(my_model)
    print(type(my_model))
    print(isinstance(my_model, BaseModel))
