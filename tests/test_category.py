import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from category import Category  # Replace 'category' and 'Category' with the actual module and class names

# Test cases for the Category class
def test_category_initialization():
	obj = Category("Test")
	assert obj is not None

if __name__ == "__main__":
	pytest.main()