#!/usr/bin/python3
import sys
from models.base_model import BaseModel

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No file")
    else:
        try:
            with open(sys.argv[1], 'r') as f:
                print("OK")
        except FileNotFoundError:
            print("No file")
