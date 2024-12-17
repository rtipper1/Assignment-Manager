class Category:
    def __init__(self, name, weight, assignments):
        self.name = name
        self.weight = weight
        self.assignments = assignments

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_assignments(self):
        return self.assignments

    def get_assignment(self, assignment_name):
        for assignment in self.assignments:
            if assignment.get_name() == assignment_name:
                return assignment
        raise ValueError("Assignment: '{assignment_name}' not found.")
        