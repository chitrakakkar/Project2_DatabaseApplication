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

CREATE TABLE Time_Sheet(
EmpLoyee_ROWID INT NOT NULL,
Hours FLOAT NOT NULL,
Date Text NOT NULL,
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


INSERT INTO Time_Sheet  VALUES (1, 8.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (2, 7.30,'2016-09-16' );
INSERT INTO Time_Sheet  VALUES (3, 8.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (4, 9.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (5, 12.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (6, 9.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (7, 6.0,'2016-09-16');
INSERT INTO Time_Sheet  VALUES (7, 8.30,'2016-09-17');
INSERT INTO Time_Sheet  VALUES (5, 10.0,'2016-09-17');



'''

try:
    print("Creating tables")
    conn = sqlite3.connect('Employee.db')
    conn.executescript(sql_script)
except sqlite3.OperationalError as oe:
    print('Error:', oe)
    print("Database already exists..Aborting")