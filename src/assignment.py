import re

class Assignment:
    def __init__(self, title, description, due_datetime, grade, completed):
        self.set_title(title)
        self.set_description(description)
        self.set_due_datetime(due_datetime)
        self.set_grade(grade)
        self.set_completed(completed)

    def __str__(self):
        return (f"Assignment(title={self.title}, description={self.description}, "
                f"due_datetime={self.due_datetime}, grade={self.grade}, completed={self.completed})")
    
    def set_title(self, title):
        if self.validate_title(title):
            self.title = title
        else:
            raise ValueError("Title must be a non-empty string")

    def set_description(self, description):
        if self.validate_description(description):
            self.description = description  
        else:
            raise ValueError("Description must be a non-empty string or None")

    def set_due_datetime(self, due_datetime):
        if self.validate_due_datetime(due_datetime):
            self.due_datetime = due_datetime
        else:
            raise ValueError("Due date must be a non-empty string or None")

    def set_grade(self, grade):
        if self.validate_grade(grade):
            self.grade = grade
        else:
            raise ValueError("Grade must be a non-negative number or None")

    def set_completed(self, completed):
        if self.validate_completed(completed):
            self.completed = completed
        else:
            raise ValueError("Completed must be a boolean or None")
        
    def toggle_completed(self):
        self.completed = not self.completed


    # Title needs to be a non-empty string
    def validate_title(self, title):
        if isinstance(title, str) and title:
            return True
        return False
    
    def validate_description(self, description):
        if description is None:
            return True
        if isinstance(description, str) and description:
            return True
        return
    
    # Due date needs to be a non-empty string or None
    def validate_due_datetime(self, due_datetime):
        

        if due_datetime is None:
            return True
        if isinstance(due_datetime, str) and re.match(r"\d{2}/\d{2}/\d{4}, \d{2}:\d{2} (AM|PM)", due_datetime):
            return True
        return False
    
    # Grade needs to be a non-negative number or None
    def validate_grade(self, grade):
        if grade is None:
            return True
        if isinstance(grade, (float, int)) and grade >= 0:
            return True
        return False
    
    # Completed must be a boolean
    def validate_completed(self, completed):
        if isinstance(completed, bool):
            return True
        return False
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_due_datetime(self):
        return self.due_datetime
    
    def get_grade(self):
        return self.grade
    
    def get_completed(self):
        return self.completed