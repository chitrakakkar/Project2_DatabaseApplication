"""
This class deals with the user interface and error checking of the input data
gives couple of menu options and define each option to perform an action.
"""


from Database_Manager import dataBase_manaGer
from Tables_Entity import SalarySlip
db = dataBase_manaGer('Employee.db')


def HR_Options(employee, payScale):
    """
        Display menu for user, checks if the user input is an integer and does
        action basis option chosen.
        """
    menu = (

        '\nOptions\n'
        '\t1)Get Employee\n'
        '\t2)Add Employee\n'
        '\t3)Delete Employee\n'
        '\t4)Update Employee Grade\n'
        '\t5)Time-Sheet\n'
        '\t6)Quit\n'
        'Choose from above mentioned options'
    )

    while True:
        Option_choice = get_employee_input_int(menu)
        if Option_choice == 1:
            get_employee(employee)
        elif Option_choice == 2:
            add_employee(employee)
        elif Option_choice == 3:
            delete_employee(employee)
        elif Option_choice == 4:
            update_employee(employee)
        elif Option_choice ==5:
            emp_salary_slip(employee,payScale)
        elif Option_choice == 6:
            exit(0);
        else:
            print("Invalid Entry !!! Please choose Option between (1-6)")
            continue
    return


def get_employee(employee):

    """Gets the employee data from the Employee table with id
     and format done for printing the data"""

    employee_id = get_employee_input_int('Enter employee ID to get the data ')
    employee = db.get_employee(employee_id)
    if not employee:
        print("No employee found with id ", employee_id)
    else:
        payscale = db.get_payScale(employee.grade)
        print('DATA:-> {} {} has grade = {} which gives {} per hours\n'
              .format(employee.first_name, employee.last_name, employee.grade, payscale.salary))


def add_employee(employee):
    """ Adds a new employee to the employee table"""

    while True:
        first_name = get_user_string("Enter your first name")
        last_name = get_user_string("Enter your last name")
        grade = get_employee_input_int("Enter your grade", range(1,7))
        db.add_employee(first_name, last_name, grade)
        print("New employee " + first_name + "" + last_name + " has been added to the employee table")
        user_input = input("Do you want to add more employees to the table ? (Y/N)")
        if(str(user_input).upper()) == 'Y':
            continue
        elif (str(user_input).upper()) == 'N':
            break
        else:
            print("Invalid Input\nReturning to the main menu")
            break


def delete_employee(employee):
    """ Delete an existing employee from the employee table"""
    employee_Id_list = db.get_employee_Id_list()
    print("The current employee list is " , employee_Id_list)
    while True:
        delete_id = get_user_string("Enter the employee id to be delete")
        if int(delete_id) in employee_Id_list:
            employee_to_be_deleted = db.get_employee(delete_id)
            db.delete_employee(delete_id)
            print("Employee " + employee_to_be_deleted.full_name + " has been delete from employee")
            break
        else:
            print("No Id found")
            continue


def update_employee(employee):
    """ Updates the grade for an existing employee to the employee table"""
    employee_id = get_employee_input_int("Enter the employee id you want to update")
    newGrade = get_employee_input_int("Enter the new grade for ", employee_id)
    db.update_employee(employee_id, newGrade)
    print(employee.full_name + "'s grade value has been update to :-> ", newGrade)


def emp_salary_slip(employee,payscale):
    """ Shows the Salary _Slip for the employee"""
    emp_id = get_employee_input_int("Enter your employee ID")
    week_Number = get_employee_input_int("Enter the week number")
    hours = get_employee_hours_Float("Enter your hours for the week")
    Total_salary = SalarySlip.get_Total_Salary(hours, payscale.salary)
    db.get_TimeSheet(emp_id, hours, week_Number, Total_salary)
    print('Employee:-> {} has a Grade = {} | Salary Slip :-> week {} |\n'
          'Total Working hours-> {} | Pay/hours -> {} | Total-Salary for this week {}'
          .format(db.get_employee(emp_id).full_name, employee.grade, week_Number, hours, payscale.salary, round(Total_salary, 2)))


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


def get_employee_input_int(message):
    """ Returns an integer from the user , else an error prompt"""
    while True:
        user_input = input('{}: '.format(message))

        # Type validation
        try:
            number = int(user_input)
            break
        except ValueError:
            print('You must enter a whole number.')
            continue

        #Range Validation
        # if valid_range and number not in valid_range:
        #     _min = min(valid_range)
        #     _max = max(valid_range)
        #     print('You must enter a number from {} to {}.'.format(_min, _max))
        #     continue
    return number


def get_employee_hours_Float(message):
    """ Returns a float number, else an error message"""
    while True:
        user_input = input('{}: '.format(message))

        # Type validation
        try:
            number = float(user_input)
            print("You entered this hour ", number)
            break
        except ValueError:
            print('You must enter a Float number.')
            continue

        #Range Validation
        # if valid_range and number not in valid_range:
        #     _min = min(valid_range)
        #     _max = max(valid_range)
        #     print('You must enter a number from {} to {}.'.format(_min, _max))
        #     continue
    return number


def main():
    """ shows the default test data and calls the menu function if all ok"""
    while True:
        employee_id = get_employee_input_int('TEST DATA: Enter employee ID to look up for the data ')
        employee = db.get_employee(employee_id)
        if not employee:
            print("No employee found with id ", employee_id)

        else:
            payscale = db.get_payScale(employee.grade)
            print('DATA:-> {} has a grade = {}, Hence gets {} per hours\n'
                  .format(employee.full_name,employee.grade, payscale.salary))
            HR_Options(employee, payscale)
            break

main()

