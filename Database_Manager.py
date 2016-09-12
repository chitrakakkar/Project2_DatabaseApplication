"""
This class sets up the database and creates required tables.  It also deals with
different methods to get data from the data base using queries.
"""
import sqlite3
from Tables_Entity import Employee, PayScale


class dataBase_manaGer:
    """Manages connecting and getting information from the database."""
    def __init__(self, filename):
        """Set up the connection to the database."""
        self.conn = sqlite3.connect(filename)

    def get_employee(self, employee_id):

        """Return a employee object from the ID if they exist, None otherwise."""
        try:
            cur = self.conn.cursor()
            query = 'SELECT ROWID,  * FROM Employee WHERE ROWID = ?  '
            # cur.execute expects a tuple for the second argument.You will get an
            # error if you only pass student_id.  Passing in (student_id, ) makes it
            # a single item tuple.  Another way to do it would be to pass in
            # tuple(student)
            cur.execute(query, (employee_id,))

            row = cur.fetchone()
            if row:
                return Employee(row[0], row[1], row[2], row[3])
            else:

                return None
        except sqlite3.OperationalError as oe:
                print('Sql execution error', oe)

        except sqlite3.Error as e:
            print("Connection error ", e)

    def get_payScale(self, grade_id):
        """Return a employee object from the ID if they exist, None otherwise."""
        try:
            cur = self.conn.cursor()
            query = 'SELECT ROWID, * FROM PayScale WHERE ROWID = ?  '
            cur.execute(query, (grade_id,))
            row = cur.fetchone()
            if row:
               return PayScale(row[0], row[1])
            else:
                return None

        except sqlite3.OperationalError as oe:
              print('Sql execution error', oe)
        except sqlite3.Error as e:
              print("Connection error ", e)

    def get_employee_Id_list(self):
        """Return a employee list from the employee table, None otherwise."""
        try:
            employee_Id_list =[]
            cur = self.conn.cursor()
            query = 'SELECT ROWID FROM Employee'
            cur.execute(query)
            for row in cur.fetchall():
                employee_id = row[0]
                employee_Id_list.append(self.get_employee(employee_id).id)
            return employee_Id_list
        except sqlite3.OperationalError as oe:
           print('Sql execution error', oe)
        except sqlite3.Error as e:
           print("Connection error ", e)

    def add_employee(self, first_name, last_name, grade):
        """ Adds new employee to the employee table """
        cur = self.conn.cursor()
        query = 'INSERT INTO Employee VALUES(?,?,?) '
        cur.execute(query, (first_name, last_name, grade))
        self.conn.commit()

    def delete_employee(self, employee_id):
        """ Deletes employee from the employee """

        try:
            cur = self.conn.cursor()
            query = 'DELETE FROM Employee WHERE ROWID = ? '
            cur.execute(query, (employee_id,))
            self.conn.commit()
        except sqlite3.OperationalError as oe:
            print('Sql execution error', oe)
        except sqlite3.Error as e:
            print("Connection error ", e)

    def update_employee(self, employee_id, newGrade):
        """Updates employee information in the table """

        try:
            cur = self.conn.cursor()
            query = 'UPDATE Employee ' \
                'SET  Grade = ?' \
                'WHERE ROWID = ? '
            cur.execute(query, (newGrade, employee_id))
            self.conn.commit()
        except sqlite3.OperationalError as oe:
            print('Sql execution error', oe)
        except sqlite3.Error as e:
            print("Connection error ", e)

    def get_TimeSheet(self, employee_id, week_Number, Hours, Total_Salary):
        """ Gets you the weekly salary for an employee"""
        try:
            cur = self.conn.cursor()
            query = 'INSERT INTO Salary_Slip(Employee_ROWID, Hours, Week, Total_Salary) VALUES ' \
                    '(?,?,?,?)'
            cur.execute(query, (employee_id, Hours, week_Number, Total_Salary))
            self.conn.commit()
        except sqlite3.OperationalError as oe:
            print('Sql execution error', oe)
        except sqlite3.Error as e:
            print("Connection error ", e)