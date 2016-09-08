import sqlite3

sql_script = '''
CREATE TABLE Employee (
FirstName TEXT,
LastName TEXT,
Grade INTEGER
);

CREATE TABLE PayScale(
GRADE INTEGER,
PAY FLOAT );

INSERT INTO Employee VALUES ('Nihal', 'Mohan','3');
INSERT INTO Employee VALUES ('Chitra', 'Kakkar','6');
INSERT INTO Employee VALUES ('Simon', 'Asher','5');
INSERT INTO Employee VALUES ('Rachel', 'Wood','7');

INSERT INTO PayScale VALUES ('1','35.67');
INSERT INTO PayScale VALUES ('2','29.23');
INSERT INTO PayScale VALUES ('3','25.07');
INSERT INTO PayScale VALUES ('4','22.13');
INSERT INTO PayScale VALUES ('5','20.17');
INSERT INTO PayScale VALUES ('6','18.00');
INSERT INTO PayScale VALUES ('7','15.00');
'''

try:
    print("Creating tables")
    conn = sqlite3.connect('Employee.db')
    conn.executescript(sql_script)
except sqlite3.OperationalError as oe:
    print('Error:', oe)
    print("Database already exists..Aborting")