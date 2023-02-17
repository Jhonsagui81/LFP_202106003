class Persona:
    def __init__(self, name, department, birthday_month):
        self.name = name
        self.department = department
        self.birthday = birthday_month

    def print_name(self):
        print(self.name)