class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_instructor(self):
        return self.instructor

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_instructor(self, instructor):
        self.instructor = instructor

# Example usage:
course = Course("Introduction to Python", "PY101", "John Doe")
print(course.get_name())  # Output: Introduction to Python
print(course.get_code())  # Output: PY101
print(course.get_instructor())  # Output: John Doe