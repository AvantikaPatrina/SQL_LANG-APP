import sqlite3
##connect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor
cursor=connection.cursor()

##create table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""
# Execute the table creation
cursor.execute(table_info)

# Insert data
insert_query = """
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS)
VALUES 
    ('Alice', '10', 'A', 85),
    ('Bob', '10', 'B', 78),
    ('Charlie', '9', 'A', 92),
    ('David', '9', 'B', 88),
    ('Eva', '8', 'A', 95)
"""

cursor.execute(insert_query)

## display
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

##Commit
connection.commit()
connection.close()