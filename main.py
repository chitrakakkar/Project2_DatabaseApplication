from Database_Manager import dataBase_manaGer

db = dataBase_manaGer('Employee.db')


def HR_Options(employee, payScale):
    menu = (
        '\nOptions\n'
        'Employee:{} {} has grade = {} which gives {} per hours\n'
        '\t1)Add Employee\n'
        '\t2)Delete Employee\n'
        '\t3)Update Employee\n'
        '\t4)Quit\n'
        'Choose from above mentioned options'
    ).format(employee.first_name, employee.last_name, employee.grade, payScale.salary)

    while True:
        Option_choice = get_employee_int(menu, None)

        if Option_choice == 1:
            add_employee(employee)
        elif Option_choice == 2:
            delete_employee(employee)
        elif Option_choice == 3:
            update_employee(employee)
        else:
            exit(0);


def add_employee(employee):
    first_name = get_user_string("Enter your first name")
    last_name = get_user_string("Enter your last name")
    grade = get_employee_int("Enter your grade", range(1,7))
    db.add_employee(first_name, last_name, grade)
    print("New employee " + first_name + last_name + " has been added to the employee table")


def delete_employee(employee):
    while True:
        delete_id = get_user_string("Enter the employee id to be delete")
        db.delete_employee(delete_id)
        print("Employee " + delete_id + " has been delete from employee")
        break


def update_employee(employee):
    employee_id = get_employee_int("Enter the employee id you want to update", range(1, 10))
    newGrade = get_employee_int("Enter the new grade for " + employee_id, range(1, 7))
    db.update_employee(employee_id, newGrade)
    print(employee_id + " grade value has been update to " + newGrade)


def get_user_string(message):
    """Return a string from the user.

       Args:
           message (str): Message to prompt the user with.

       """
    while True:
        user_input = input('{}: '.format(message))
        # This is a bad way to check if the user input is not empty.
        # It will be True if the user enters spaces, tabs, etc.
        if user_input:
            return user_input
        else:
            print('You must enter something.')


def get_employee_int(message, valid_range=None):
    while True:
        user_input = input('{}: '.format(message))

        # Type validation
        try:
            number = int(user_input)
        except ValueError:
            print('You must enter a whole number.')
            continue

        #Range Validation
        if valid_range and number not in valid_range:
            _min = min(valid_range)
            _max = max(valid_range)
            print('You must enter a number from {} to {}.'.format(_min, _max))
            continue
        return number


def main():
    employee_id = get_employee_int('Enter employee ID ')
    employee = db.get_employee(employee_id)
    payscale = db.get_payScale(employee.grade)
    if not employee:
        print("No employee found with id ", employee_id)
    else:
        HR_Options(employee, payscale)

main()

