import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_review_creation(self):
        """Test if Review instance is created correctly"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test Review attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
