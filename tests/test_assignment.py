import unittest
from modules.Assignment import Assignment

class TestAssignment(unittest.TestCase):
    assignment = Assignment("Default", 10, "10/12/2024 11:59:00", None, False)

    def test_set_name():

        

if __name__ == '__main__':
    unittest.main()