import sqlite3
from Tables_Entity import Employee, PayScale


class dataBase_manaGer:

    """Manages connecting and getting information from the database."""
    def __init__(self, filename):
        """Set up the connection to the database."""
        self.conn = sqlite3.connect(filename)

    def get_employee(self, employee_id):
        cur = self.conn.cursor()
        query = 'SELECT ROWID, * FROM Employee WHERE ROWID = ?  '
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

    def get_payScale(self, grade_id):
        cur = self.conn.cursor()
        query = 'SELECT ROWID, * FROM PayScale WHERE ROWID = ?  '
        cur.execute(query, (grade_id,))
        row = cur.fetchone()
        if row:
            return PayScale(row[0], row[1])
        else:
            return None

    def get_employee_Id_list(self):
        employee_Id_list =[]
        cur = self.conn.cursor()
        query = 'SELECT ROWID FROM Employee'
        cur.execute(query)
        for row in cur.fetchall():
            employee_id = row[0]
            employee_Id_list.append(self.get_employee(employee_id).id)
        return employee_Id_list


    # def get_all_employee_list(self):
    #     employee_list =[]
    #     cur = self.conn.cursor()
    #     query = 'SELECT ROWID, * FROM Employee '
    #     cur.execute(query)
    #     for row in cur.fetchall():
    #         employee_id = row[1]
    #         employee_list.append(self.get_employee(employee_id))
    #     return employee_list


    def add_employee(self, first_name, last_name, grade):
        """ Adds new employee to the employee table """
        cur = self.conn.cursor()
        query = 'INSERT INTO Employee VALUES(?,?,?) '
        cur.execute(query, (first_name, last_name, grade))
        self.conn.commit()



    def delete_employee(self,employee_id):
        """ Deletes employee from the employee """
        cur = self.conn.cursor()
        query = 'DELETE FROM Employee WHERE ROWID = ? '
        cur.execute(query, (employee_id,))
        self.conn.commit()

    def update_employee(self, employee_id, newGrade):
        """Updates employee information in the table """
        cur = self.conn.cursor()
        query = 'UPDATE Employee ' \
                'SET  Grade = ?' \
                'WHERE employee_id = ? '
        cur.execute(query,(employee_id, newGrade))
        self.conn.commit()

