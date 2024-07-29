import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from assignment import Assignment

# Test cases for the Assignment class
def test_assignment():
    assert True

if __name__ == "__main__":
    pytest.main()