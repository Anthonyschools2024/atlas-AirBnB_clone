#!/usr/bin/python3
import sys
import json
from models.base_model import BaseModel


def test_save(file_path):
    """Test the save method of BaseModel."""
    model = BaseModel()
    model.save()  # Save the object

    # Check if the save() method creates the expected file
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            if any("BaseModel" in key for key in data):
                print("OK")
            else:
                print("No data")
    except FileNotFoundError:
        print("No file")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./test_fake_base_model.py <file_path>")
    else:
        test_save(sys.argv[1])
