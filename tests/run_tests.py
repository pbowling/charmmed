import unittest
from os import path

if __name__ == "__main__":
    test_path = path.abspath(__file__)
    test_path = path.dirname(test_path)

    suite = unittest.TestLoader().discover(test_path)
    unittest.TextTestRunner().run(suite)