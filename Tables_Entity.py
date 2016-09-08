"""These classes are used to help bundle the data from the database."""


class Employee:
    def __init__(self, employee_id, first_name, last_name, grade):
        self.id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade


class PayScale(Employee):
        def __init__(self, employee_id, first_name, last_name, grade):
            Employee.__init__(self, employee_id, first_name, last_name, grade)  # Salary class inheriting from Employees

            if self.grade == 1:
                self.salary_scale = 35.67

            if self.grade == 2:
                self.salary_scale = 29.23

            if self.grade == 3:
                self.salary_scale = 25.07

            if self.grade == 4:
                self.salary_scale = 22.13

            if self.grade == 5:
                self.salary_scale = 20.17

            if self.grade == 6:
                self.salary_scale = 18.00

            if self.grade == 7:
                self.salary_scale = 15.00
