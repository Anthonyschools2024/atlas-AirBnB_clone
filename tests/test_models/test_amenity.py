import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_amenity_creation(self):
        """Test if Amenity instance is created correctly"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name(self):
        """Test Amenity name attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
