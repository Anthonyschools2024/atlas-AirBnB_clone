import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_state_creation(self):
        """Test if State instance is created correctly"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name(self):
        """Test State name attribute"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
