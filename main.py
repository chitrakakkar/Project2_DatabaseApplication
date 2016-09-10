from Database_Manager import dataBase_manaGer

db = dataBase_manaGer('Employee.db')


def HR_Options(employee):
    menu = (

        '\nOptions\n'
        '\t1)Add Employee\n'
        '\t2)Delete Employee\n'
        '\t3)Update Employee\n'
        '\t4)Quit\n'
        'Choose from above mentioned options'
    )

    while True:
        Option_choice = get_employee_id_int(menu, None)

        if Option_choice == 1:
            add_employee(employee)
        elif Option_choice == 2:
            delete_employee(employee)
        elif Option_choice == 3:
            update_employee(employee)
        else:
            exit(0);


def add_employee(employee):
    while True:
        first_name = get_user_string("Enter your first name")
        last_name = get_user_string("Enter your last name")
        grade = get_employee_id_int("Enter your grade", range(1,7))
        db.add_employee(first_name, last_name, grade)
        print("New employee " + first_name +"\t" + last_name + " has been added to the employee table")
        user_input=input("Do you want to add more employees to the table ? (Y/N)")
        if(str(user_input).upper()) == 'Y':
            continue
        elif (str(user_input).upper()) == 'N':
            break
        else:
            print("Invalid Input\nReturning to the main menu")
            break


def delete_employee(employee):
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
    employee_id = get_employee_id_int("Enter the employee id you want to update")
    newGrade = (get_employee_id_int("Enter the new grade for " + employee_id))
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


def get_employee_id_int(message, valid_range=None):
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
    while True:
        employee_id = get_employee_id_int('Enter employee ID to look up the data ')
        employee = db.get_employee(employee_id)
        if not employee:
            print("No employee found with id ", employee_id)

        else:
            payscale = db.get_payScale(employee.grade)
            print('DATA:-> {} {} has grade = {} which gives {} per hours\n'
                  .format(employee.first_name, employee.last_name, employee.grade, payscale.salary))
            HR_Options(employee)
            break

main()

