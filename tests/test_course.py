import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from course import Course  # Replace 'my_class' and 'MyClass' with the actual module and class names

# Test cases for the MyClass class
def test_my_class_initialization():
	obj = Course("Python Programming", "PY101", "John Doe")
	assert obj is not None

if __name__ == "__main__":
	pytest.main()