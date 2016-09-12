"""These classes are used to help bundle the data from the database."""


class Employee:
    def __init__(self, employee_id, first_name, last_name, grade):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class PayScale:

    def __init__(self, grade, salary):
        self.grade = grade
        self.salary = salary
        if self.grade == 1:
            self.salary = 35.67

        if self.grade == 2:
            self.salary = 29.23

        if self.grade == 3:
            self.salary = 28.90

        if self.grade == 4:
            self.salary = 30.00

        if self.grade == 5:
            self.salary = 22.52

        if self.grade == 6:
            self.salary = 22.12

        if self.grade == 7:
            self.salary = 24.56


class SalarySlip:

    def __init__(self, employee_id, week, Hours):
        self.employee_id = employee_id
        self.week = week
        self.Hours = Hours

    def get_Total_Salary(hours, salary):
        Total_Salary = hours * salary
        return Total_Salary





