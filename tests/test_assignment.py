import sys
import os
import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from assignment import Assignment

# Test cases for the Assignment class
import pytest
from assignment import Assignment

def test_set_title():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    
    # Test invalid title
    with pytest.raises(ValueError, match="Title must be a non-empty string"):
        assignment.set_title("")
        assignment.set_title(None)
    
    assignment.set_title("Assignment 2")
    assert assignment.title == "Assignment 2"

def test_set_description():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    
    # Test invalid description
    with pytest.raises(ValueError, match="Description must be a non-empty string or None"):
        assignment.set_description("")
    
    assignment.set_description("Description 2")
    assert assignment.description == "Description 2"

def test_set_due_datetime():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    
    # Test invalid due_date
    with pytest.raises(ValueError, match=r"Due date must be a non-empty string of format 'MM/DD/YYYY, HH:MM \(PM\|AM\)' or None"):
        assignment.set_due_datetime("")
    
    assignment.set_due_datetime("07/30/2024, 11:59 PM")
    assert assignment.due_datetime == "07/30/2024, 11:59 PM"

def test_set_grade():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    
    # Test invalid grade
    with pytest.raises(ValueError, match="Grade must be a non-negative number or None"):
        assignment.set_grade(-1)
    
    assignment.set_grade(90)
    assert assignment.grade == 90

def test_set_completed():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    
    # Test invalid completed
    with pytest.raises(ValueError, match="Completed must be a boolean or None"):
        assignment.set_completed("not a boolean")
    
    assignment.set_completed(True)
    assert assignment.completed == True

def test_initialization():
    # Test valid initialization
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    assert assignment.title == "Assignment 1"
    assert assignment.description == "Description 1"
    assert assignment.due_datetime == "07/30/2024, 11:59 PM"
    assert assignment.grade == 100
    assert assignment.completed == False

    # Test invalid initialization
    with pytest.raises(ValueError, match="Title must be a non-empty string"):
        Assignment("", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    with pytest.raises(ValueError, match="Description must be a non-empty string or None"):
        Assignment("Assignment 1", "", "07/30/2024, 11:59 PM", 100, False)
    with pytest.raises(ValueError, match=r"Due date must be a non-empty string of format 'MM/DD/YYYY, HH:MM \(PM\|AM\)' or None"):
        Assignment("Assignment 1", "Description 1", "", 100, False)
    with pytest.raises(ValueError, match="Grade must be a non-negative number or None"):
        Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", -1, False)
    with pytest.raises(ValueError, match="Completed must be a boolean or None"):
        Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, "not a boolean")

def test_toggle_completed():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    assignment.toggle_completed()
    assert assignment.completed == True
    assignment.toggle_completed()
    assert assignment.completed == False

def test_getters():
    assignment = Assignment("Assignment 1", "Description 1", "07/30/2024, 11:59 PM", 100, False)
    assert assignment.get_title() == "Assignment 1"
    assert assignment.get_description() == "Description 1"
    assert assignment.get_due_datetime() == "07/30/2024, 11:59 PM"
    assert assignment.get_grade() == 100
    assert assignment.get_completed() == False

if __name__ == "__main__":
    pytest.main(["-s"])
