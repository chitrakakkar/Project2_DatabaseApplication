"""These classes are used to help bundle the data from the database."""


class Employee:
    def __init__(self, employee_id, first_name, last_name, grade):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade


class PayScale:
    # def __init__(self, employee_id, first_name, last_name, grade):
    #     Employee.__init__(self, employee_id, first_name, last_name, grade)  # Salary class inheriting from Employees

    def __init__(self, grade, salary):
        self.grade = grade
        self.salary = salary
        if self.grade == 1:
            self.salary = 35.67

        if self.grade == 2:
            self.salary = 29.23

        if self.grade == 3:
            self.salary = 25.07

        if self.grade == 4:
            self.salary = 22.13

        if self.grade == 5:
            self.salary = 20.17

        if self.grade == 6:
            self.salary = 18.00

        if self.grade == 7:
            self.salary = 15.00
