import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def test_save(self):
        """Test that save() method updates `updated_at` attribute"""
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(1)  # Pause for 1 second to see the change in time
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > old_updated_at)

    def test_str(self):
        """Test the __str__ method to ensure correct output format"""
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
