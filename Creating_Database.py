"""Run a SQL script where a set of commands are saved in a
        # file/string/script creates tables and inserts value to set up the database."""

import sqlite3

sql_script = '''

CREATE TABLE Employee (
FirstName TEXT NOT NULL ,
LastName TEXT NOT NULL,
Grade INTEGER NOT NULL,
FOREIGN KEY (Grade) REFERENCES PayScale(ROWID)
);

CREATE TABLE PayScale(
Grade INTEGER,
PAY_PerHour FLOAT );

CREATE TABLE Salary_Slip(
EmpLoyee_ROWID INT NOT NULL,
Hours FLOAT NOT NULL,
WEEK INTEGER NOT NULL,
Total_Salary DOUBLE NOT NULL,
FOREIGN KEY (EmpLoyee_ROWID) REFERENCES Employee(ROWID)
);


INSERT INTO Employee VALUES ('Nihal','Mohan',3);
INSERT INTO Employee VALUES ('Chitra', 'Kakkar',6);
INSERT INTO Employee VALUES ('Simon', 'Asher', 5);
INSERT INTO Employee VALUES ('Rachel', 'Wood',7);
INSERT INTO Employee VALUES ('Sarah', 'Smith',3);
INSERT INTO Employee VALUES ('Gordon', 'White',5);
INSERT INTO Employee VALUES ('Tina', 'Scott',5);



INSERT INTO PayScale VALUES (1,35.06);
INSERT INTO PayScale VALUES (2,29.07);
INSERT INTO PayScale VALUES (3,28.90);
INSERT INTO PayScale VALUES (4,30.00);
INSERT INTO PayScale VALUES (5,22.52);
INSERT INTO PayScale VALUES (6,22.12);
INSERT INTO PayScale VALUES (7,24.56);


INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (1, 45.0, 1, 1128.15);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (2, 40.0, 1, 720.00);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (3, 38.0, 1, 766.46);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (4, 39.0, 1, 585.00);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (5, 50.0, 1, 1253.07);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (6, 40.0, 1, 806.8);
INSERT INTO Salary_Slip (EmpLoyee_ROWID,Hours,WEEK,Total_Salary) VALUES (7, 42.0, 1, 869.00);


'''

try:
    print("Creating tables")
    conn = sqlite3.connect('Employee.db')
    conn.executescript(sql_script)
except sqlite3.OperationalError as oe:
    print('Error:', oe)
    print("Database already exists..Aborting")