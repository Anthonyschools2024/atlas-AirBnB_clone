import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test if BaseModel instance is created correctly"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at(self):
        """Test that created_at is a datetime object"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
