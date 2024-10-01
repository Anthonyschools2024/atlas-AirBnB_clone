from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system, inherits from BaseModel"""
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
