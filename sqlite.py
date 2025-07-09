import sqlite3

## Connecting wiht sqllite
connection=sqlite3.connect("students.db")

## Creating a cursor object to insert record and create table
cursor=connection.cursor()

## Creating the table
table_info="""
    CREATE TABLE STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
    );
"""

cursor.execute(table_info)

## Insert the values
cursor.execute('''INSERT INTO STUDENT VALUES('KRISH','Data Science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('John','Data Science','B',100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mukesh','Data Science','A',86)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Jacob','DEVOPS','A',50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Dipesh','DEVOPS','A',35)''')

## Display the records
print("The inserted records are -----> ")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit all the changes
connection.commit()
connection.close()