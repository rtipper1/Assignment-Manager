class Course:
    def __init__(self, name, credit_hours, categories):
        self.name = name
        self.credit_hours = credit_hours
        self.categories = categories

    def add_category(self, category):
        self.categories.append(category)

    def add_assignment_to_category(self, assignment, category_name):
        for category in self.categories:
            if category.get_name() == category_name:
                category.add_assignment(assignment)
                return
        raise ValueError("Category: '{category_name}' not found.")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_credit_hours(self):
        return self.credit_hours

    def set_credit_hours(self, credit_hours):
        self.credits = credit_hours

    def get_categories(self):
        return self.categories

    def set_categories(self, categories):
        self.categories = categories

    def get_category(self, category_name):
        for category in self.categories:
            if category.get_name() == category_name:
                return category
        raise ValueError("Category: '{category_name}' not found.")