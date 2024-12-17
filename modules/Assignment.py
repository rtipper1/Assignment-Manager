from datetime import datetime

class Assignment:
    def __init__(self, name, points, due_date, grade, dropped):
        self.name = name
        self.points = points
        self.due_date = due_date
        self.grade = grade
        self.dropped = dropped


    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name

        
    def get_name(self):
        return self.name


    def set_points(self, points):
        if not isinstance(points, float):
            raise TypeError("Points must be a float")
        self.points = points


    def get_points(self):
        return self.points


    def set_due_date(self, due_date):
        try:
            self.due_date = datetime.strptime(due_date, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            raise ValueError("Due date must be in DD/MM/YYYY HH:MM:SS format")


    def get_due_date(self):
        return self.due_date


    def set_grade(self, grade):
        if not (0 < grade < 1):
            raise ValueError("Grade must be between 0 and 1")
        self.grade = grade


    def get_grade(self):
        return self.grade
    

    def set_dropped(self, dropped):
        if not isinstance(dropped, bool):
            raise TypeError("Dropped must be a boolean")
        self.dropped = dropped


    def get_dropped(self):
        return self.dropped