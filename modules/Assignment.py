class Assignment:
    def __init__(self, name, points, due_date, grade):
        self.name = name
        self.points = points
        self.due_date = due_date
        self.grade = grade

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points

    def get_due_date(self):
        return self.due_date

    def set_due_date(self, due_date):
        self.due_date = due_date

    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade