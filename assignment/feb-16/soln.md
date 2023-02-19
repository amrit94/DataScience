## 16 Feb Assignment Solution 

### Q1. What is a database? Differentiate between SQL and NoSQL databases.

Database is an electronic place/system where `data is stored` in a way that it can be easily accessed, managed, and updated.
It is also used to `organize the data` in the form of a table, schema, views, and reports, etc.

SQL and NoSQL databases

* Relation
  * SQL is a `relational` database management system.
  * NoSQL is a `non-relational` or distributed database management system
* Model
  * SQL follows the `ACID model`
  * No-SQL follows the `BASE model`
* Database type
  * SQL is in the form of `tables`, i.e., in the form of rows and columns.
  * NoSQL is in the form of documents, `key-value`, and graphs.
* Data Type
  * SQL is not the best choice for storing hierarchical data
  * NoSQL database is a perfect option for `storing hierarchical data`
* Scaling
  * SQL - esay vertical scaling, difficult horizantal scaling
  * NoSQL - easy vertical and horizantal scaling




### Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.

DDL stands for Data Definition Language

Query statements are DDL, that `define databases, tables & table structures` (CREATE DATABASE, CREATE TABLE) or `manage database & table` (ALTER DATABASE, DROP DATABASE, ALTER TABLE, DROP TABLE)

DDL basically defines the column of the table. DML is used to create database schema 

* CREATE - generates a new table
```
CREATE TABLE Student_info (
    College_Id number(2),
    College_name varchar(30),
    Branch varchar(10)
);
```

* ALTER - add, delete or change columns in the existing table
```
ALTER TABLE Student_info ADD CGPA number;
```

* TRUNCATE -  remove all rows from the table, but the structure of the table still exists.
```
TRUNCATE TABLE Student_info;
```

* DROP - remove an existing table along with its structure from the Database
```
DROP TABLE Student_info;
```


### Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.

DML stands for Data Manipulation Language

Query statements that `manipulate or fetch data` (UPDATE, INSERT, MERGE etc.)

DML add or update the row of the table. DML is used to add, retrieve or update the data.

* INSERT - insert data in database tables.
```
INSERT INTO Student (Stu_id, Stu_Name, Stu_Marks, Stu_Age) VALUES (104, Anmol, 89, 19);  
```
* UPDATE - update or modify the existing data in database tables.
```
UPDATE Product SET Product_Price = 80 WHERE Product_Id = 'P102';
```
* DELETE - remove single or multiple existing records from the database tables.
```
DELETE FROM Product WHERE Product_Id = 'P202' ;
```


### Q4. What is DQL? Explain SELECT with an example.

DQL stands for Data Query Language, DQL statements are used for performing queries on the data within schema objects.

* SELECT - shows the records of the specified table
```
SELECT * FROM Student;  
```


### Q5. Explain Primary Key and Foreign Key.

A column or columns is called primary key (PK) that uniquely identifies each row in the table.

A foreign key is a field or a column that is used to establish a link between two tables. A foreign key in one table used to point primary key in another table.


### Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

To execute a SQL query in Python, we need to use a cursor, which abstracts away the access to database records.

MySQL Connector/Python provides you with the MySQLCursor class, which instantiates objects that can execute MySQL queries in Python. An `instance of the MySQLCursor class is also called a cursor`.


A query that needs to be executed is sent to `cursor.execute()` in string format.

```
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("select * from test1.test_table")
for i in mycursor.fetchall():
    print(i)

mydb.close()
```


### Q7. Give the order of execution of SQL clauses in an SQL query.

| Order	| Clause		| Function	| 
| :------ |:--- | :--- |
| 1	| FROM	| Tables are joined to get the base data.| 
| 2	| WHERE	| The base data is filtered.| 
| 3	| GROUP BY	| The filtered base data is grouped.| 
| 4	| HAVING	| The grouped base data is filtered.| 
| 5	| SELECT	| The final data is returned.| 
| 6	| ORDER BY	| The final data is sorted.| 
| 7	| LIMIT	| The returned data is limited to row count.| 