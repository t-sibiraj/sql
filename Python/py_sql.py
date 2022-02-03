#Module name aliasing
'''
>>>import math as m    #we can use m or whatever identifier name (identifier naming rules apply)
>>> m.floor(1.2)
1
'''

#Importing a particular function from a module

'''>>>from math import floor
   >>>floor(1.2)
   1                                           '''

#Importing every funtion from a module

''' >>>from math import * 
    >>>floor(1.2)
       1
    >>>ceil(1.2)
    2          '''



## MYSQL    CONNECTOR
#import the module

import mysql.connector as connector

### CONNECTING    TO   MySQL   DATABASE
''' SYNTAX:  variable_name = mysql.conncetor.connect(host="host_name",
						user="user_name",
						passwd  = "your_password",
						databse = name_of_the_database)      '''

'''
host ---> It is the host name or the IP address of the database serevr. As our database is a local database we can use localhost

user ---> the username you have on MySQL

password ---> the password which you have set

database ---> this is optional. You should key in the name of the databse
'''

#mysql.conncetor as connector
CODE: connection = connector.connect(host="localhost",  user="root", passwd  = "root",
                               database = "db")

#==========================================================================================


#TO CHECK IF THE CONNECTION TO THE DATABASE IS SUCCESSFUL WE CAN USE .is_connected() METHOD

'''  SYNTAX: connection_object.is_connected() ---> True ----> Successfully Connected
					   ---> False ----> Unsuccessful Connection
     CODE:
     >>> connector.is_connected()                                                              '''
True


### CREATING    A   CURSOR    INSTANCE


#WE MUST USE CURSOR IF WE WANT TO PERFORM ROW BY ROW PROCESSING

#The output for our query get stored in the cursor we can access single or multiple rows at a time from it .(This will get clear when we study about fetchall(), fetchone()). 

#The output for our query is called the resultset
#============================================================================================

#import mysql.conncetor as connector
#connection = connector.connect(details)

'''
SYNTAX: cursor_object = connection_object.cursor()

CODE:   cursor = connection.cursor()
'''

### RECORDS    TABLE:

'''
+-----+--------------+------------------+------+-------------+
| sno | student_name | email            | year | column_name |
+-----+--------------+------------------+------+-------------+
|   1 | ram          | ram@gmail.com    | 2004 |          10 |
|   2 | sam          | sam@yahoo.com    | 2003 |          20 |
|   3 | hari         | hari@outlook.com | 2002 |          30 |
|   4 | ramu         | ramu@gmail.com   | 2004 |          20 |
+-----+--------------+------------------+------+-------------+
'''



### EXCECUTING     QUERIES

'''
SYNTAX: cursor_object.execute(your_sql_query)

CODE:   cursor.execute("SELECT * FROM records")

Note: -> The output that is the retrieved ,to be precise the resultset is now stored in the cursor
      -> result set ---> output for your query
'''
#We need the include the query within quotes and pass that string  to cursor.execute()


### ACCESSING   STORED   RESULTSET(OUTPUT)   FROM    THE   CURSOR_OBJECT


#fetchall()  ---> RETURNS ALL THE ROW FROM THE RESULT SET(OUTPUT FOR YOUR QUERY)

'''
CODE:
    print(cursor.fetchall)

OUTPUT:
       [(1, 'ram', 'ram@gmail.com', 2004, 10), (2, 'sam', 'sam@yahoo.com', 2003, 20), (3, 'hari', 'hari@outlook.com', 2002, 30), (4, 'ramu', 'ramu@gmail.com', 2004, 20)]
'''
#resultset is in the form of a list of rows(these rows are in the form of tuples)
#**NOTE: ONCE WE USE FETCH ALL WE NEED TO AGAIN EXECUTE THE QUERY USING cursor.execute(query)**
#===================================================================================================

#STORING THE RESULT SET IN A VARIABLE
'''
CODE:
     cursor.execute("SELECT * FROM records")
     resultset = cursor.fetchall()  #resultset is in the form of a list
     print(resultset)

OUTPUT:
        [(1, 'ram', 'ram@gmail.com', 2004, 10), (2, 'sam', 'sam@yahoo.com', 2003, 20), (3, 'hari', 'hari@outlook.com', 2002, 30), (4, 'ramu', 'ramu@gmail.com', 2004, 20)]
'''
#===================================================================================================

#ACCESSING INDIVIDUAL ROWS

'''CODE:
    cursor.execute("SELECT * FROM records")
    row1 = cursor.fetchall()[0]
    print(row1)

OUTPUT:
        (1, 'ram', 'ram@gmail.com', 2004, 10)
'''
#===================================================================================================

#TRAVERSING AND PRINTING ALL THE ROWS
'''
CODE:
     cursor.execute("SELECT * FROM records")
     rows = cursor.fetchall()
     for row in rows:
     	print(row)
 
OUTPUT:
        (1, 'ram', 'ram@gmail.com', 2004, 10)
        (2, 'sam', 'sam@yahoo.com', 2003, 20)
        (3, 'hari', 'hari@outlook.com', 2002, 30)
        (4, 'ramu', 'ramu@gmail.com', 2004, 20)
'''


#fetchmany()   ---> Can be use to retrieve a particular number of rows

#RETRIEVE 2 RECORD FROM record TABLE
'''
CODE:
    cursor.execute("SELECT * FROM records")
    two_record = cursor.fetchmany(2)
    print(two_record)

OUTPUT:
      [(1, 'ram', 'ram@gmail.com', 2004, 10), (2, 'sam', 'sam@yahoo.com', 2003, 20)]
'''
#NOTE: The rows are in the form of a tuple inside a list
#WE CAN'T AGAIN FETCH THE FIRST TWO RECORDS. TO DO THAT WE SHOULD AGAIN EXECUTE QUERY FROM FIRST
#===================================================================================================
'''
CODE:
    cursor.execute("SELECT * FROM records")
    two_record = cursor.fetchmany(2)       #first two rows
    print(two_record)
    next_two_record = cursor.fetchmany(2)   #last two rows
    print(next_two_record)
    no_more_rows = cursor.fetchmany(2)   #As there is no more row to fetch , empty list is stored
    print(no_more_rows)

OUTPUT:
    [(1, 'ram', 'ram@gmail.com', 2004, 10), (2, 'sam', 'sam@yahoo.com', 2003, 20)]
	[(3, 'hari', 'hari@outlook.com', 2002, 30), (4, 'ramu', 'ramu@gmail.com', 2004, 20)]
	[]
'''


#fetchone() ---> Can be used when we want to fetch one single row

#FETCH A ROW FROM records TABLE
'''
CODE: 
    cursor.execute("SELECT * FROM records")
    only_one_row = cusor.fetchone()
    print(only_one_row)

OUTPUT:
      (1, 'ram', 'ram@gmail.com', 2004, 10)
      
'''

### rowcount()


#rowcount()  ---> Can be used to know how many records(rows) have been retrieved so far
			#----> It takes account of the previous retrievals
'''
CODE:
    cursor.execute("SELECT * FROM records")
    
    row1 = cursor.fetchone()
    print("Rows(records) retrieved so far",cursor.rowcount())  #1
    
    row2 = cursor.fetchone()
    print("Rows(records) retrieved so far",cursor.rowcount())  #2
    
    row3 = cursor.fetchmany(2)
    print("Rows(records) retrieved so far",cursor.rowcount())  #4
    

OUTPUT:
    Rows(records) retrieved so far 1
    Rows(records) retrieved so far 2
    Rows(records) retrieved so far 4
    
===================================================================================================
'''
#IF YOU RUN INTO ERROR:
'''
DOCS:
    1. https://dev.mysql.com/doc/connector-python/en/connector-python-tutorial-cursorbuffered.html
    2. https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-rowcount.html
FORUMS:
    1. https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone
    2. https://arrayoverflow.com/question/python-mysql-connector-errors-internalerror-unread-result-found/3196
'''

### connection_name.close()


#After retreiving the records and using the database we must close the connection

#To do that use the following command

connection.close()




## PYMYSQL

'''
WE CAN DO SAME WITH ANOTHER LIBRARY CALLED PYMYSQL

pymysql vs mysql.connector:
		---> pymysql purely written in python and made by python
		---> mysql.connecotr made by oracle
'''


#import pymysql

import pymysql as pym

#TO CREATE A CONNECTION(i.e TO CONNECT TO A DATABASE) 

'''
SYNTAX: connection_name = pymysql.connect("host_name"  , "user_name"  ,"password" ,"database")
CODE:   connection       = pym.connect(     "localhost" ,  "root"      ,"root"     ,"db")
'''

#TO TEST IF THE CONNECTION TO THE DATABASE WAS SUCCESSFULL
connection.is_connected()

#NOTE: THE THE FOLLWOING STEPS ARE SAME LIKE mysql.connector library
#TO CREATE A CUROSR OBJECT
cursor = connection.cursor()

#TO EXCECUTE QUERIES
cursor.excecute("SELECT * FROM records")

#TO FETCH ROWS FROM RESULT SET(OUTPUT)
rows = cursor.fetchmany()

#TO DISPLAY THE ROWS(RECORDS)
for row in rows:
	print(rows)
	
	
#ROWCOUNT()
count = cursor.rowcount()


### PARAMETERISED   QUERIES

'''
We provide some parameters or values from outside(by using function like input()) to run few queries

These queries are called as parameterised queries
'''

#### STRING   FORMATTING


#Before we learn about parameterised queries we must know what string formatting is.

#NEW WAY TO FORMAT STRINGS

''' "{}".format() --> Value inside the bracket gets substituted in the set bracket
			 --> The set brackets are called as placeholders                 '''

'''
>>>details = "My name is {} and I am {} years old".format("ram" , 20)
>>>print(details)
My name is ram and I am 20 years old
'''
#ram goes into the first set bracket and 20 into the second

'''
>>>details = "My name is {} and I am {} years old".format(20,"ram")
>>>print(details)
My name is 20 and I am ram years old
'''
#20 goes into the first set bracket and ram into the second
#===================================================================================================
'''

>>>details = "My name is {0} and I am {1} years old".format("ram" , 20)
>>>print(details)
My name is ram and I am 20 years old
'''
#ram is in zeroth index and 20 is in 1st index

'''
>>>details = "My name is {1} and I am {0} years old".format(20,"ram")
>>>print(details)
My name is 20 and I am ram years old
'''
'''ram is in zeroth index and 20 is in 1st index. As we have used 1st index first , the value in the 1st index ("ram") gets substituted in the set bracket'''
#===================================================================================================

'''
>>>details = "My name is {name} and I am {age} years old".format(age = 20,name = "ram")
>>>print(details)
My name is ram and I am 20 years old
'''
#now we have named the placeholder values as name and age.

#===================================================================================================


#Example:
    #Write a program in python where you should get year from the user and display the details of the that student whose year is greater than the given year. The details of the students are stored in a database
  
#CODE:
import mysql.connector as connector
connection = connector.connect(host="localhost",  user="root", passwd  = "root", database = "db")
cursor = connection.cursor()
year = input("Enter the year:")
cursor.execute("SELECT * FROM records WHERE year > {}".format(year))
print(cursor.fetchall())
connector.close()
#OUTPUT:
'''
Enter the year:2003
[(1, 'ram', 'ram@gmail.com', 2004, 10), (4, 'ramu', 'ramu@gmail.com', 2004, 20)]
'''

#OLD WAY TO FORMAT STRINGS (COMING SOON)


### cursor.commit()


#We should use cursor.commit() whenever we do some changes in the databse

#So far we have only been retrieving the records(rows) from the database

#But when we execute queries which modify the database we must use the cursor.commit() to save changes in the database()

cursor.commit()




### INSERTING    RECORDS   USING   MYSQL.CONNECTOR()    ----> IMPORTANT


#Creaing a cursor
import mysql.connector as connector
connection = connector.connect(host="localhost",  user="root", passwd  = "root", database = "db")
cursor = connection.cursor()


#we should use cursor.commit()  ---> As we are changing the database(i.e inserting records)

#inserting records 

cursor.execute("INSERT INTO records Values(1, 'som', 'som@gmail.com' ,2005 ,40)")
cursor.commit()
connector.close()
#===================================================================================================
#									(OR)
#====================================================================================================

query = "INSERT INTO records Values(1, 'som', 'som@gmail.com' ,2005 ,40)"
cursor.execute(query)
cursor.commit()
connector.close()
#===================================================================================================
#									(OR)
#====================================================================================================
#Using parameterised queries

#getting the input
sno  = int(input("Enter the sno:"))
name = input("Enter the student name:")
email = input("Enter the email:")
year = int(input("Enter the year of birth:"))
column_name = int(input("Eneter the column_name value:")
                  
#executing query
query = "INSERT INTO records Values({} , {} , {} , {} , {})".format(sno,name,email,year,column_name)
cursor.execute(query)
cursor.commit()
connector.close()                  
#We need the include the query within quotes and pass that string  to cursor.execute()


### UPDATING  RECORDS  USING   MYSQL.CONNECTOR() 


#Creaing a curosor
import mysql.connector as connector
connection = connector.connect(host="localhost",  user="root", passwd  = "root", database = "db")
cursor = connection.cursor()

#UPDATING RECORDS

query = '''UPDATE records SET year  = 2004
		WHERE year = 2002 '''              #year 2002 gets updated with a value of 2004 
cursor.execute(query)
cursor.commit()                              #use commit() to save changes
connector.close()

#===================================================================================================
#									(OR)
#====================================================================================================

#Using parameterised queries
year_old = int(input("Enter the year which needs to be updated:"))
year_new = int(input("Enter the new value for the year:"))

query = "UPDATE record SET year = {} WHERE year = {}".format(year_old , year_new)
cursor.execute(query)
cursor.commit()
connector.close()


### DELETING   RECORDS  USING   MYSQL.CONNECTOR()   --->    IMPORTANT


#Creaing a curosor
import mysql.connector as connector
connection = connector.connect(host="localhost",  user="root", passwd  = "root", database = "db")
cursor = connection.cursor()

#DELETING RECORDS

query = "DELETE FROM records WHERE name = 'ram' "
cursor.execute(query)
cursor.commit()
connector.close()
#We should use commit() as we are modifying the database. To save changes we should use cursor.commit()

#===================================================================================================
#									(OR)
#====================================================================================================

#using parameterised queries

name = input("Enter the name of student whose record you wish to be deleted:")
query = "DELETE FROM records WHERE name = {}".format("name")
cursor.execute(query)
cursor.commit() 
connector.close()


### SIMILARITY  BETWEEN  mysql.connector()  and python

'''
fetchall()     ---> readalines()
fetchone()     ---> readline()
fetchmany(n)    ---> read(n).split()

all the fetch method works in linear fashion

once we access the first two rows we have only access to the next rows not the previous rows

when you open a text file and add or delete some data it''s the same like  adding or deleting reocrds using execute

But we mush hit the save button before closing the text file to save the changes. If we don''t do that our chnages won''t get updated in the text files. To do the same in mysql.connector() we have the commit() method. It acts like a save button.

connector_name.close()  ---> It is the same like closing the text file which we have opened.
'''

## TABLES   USED

'''
records:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+

records3:
        +------+------+---------+
        | name | year | present |
        +------+------+---------+
        | ram  | 2001 | present |
        | sam  | 2002 | present |
        | ramu | 2003 | NULL    |
        +------+------+---------+

test_table:
            +------+------+---------+
            | name | year | present |
            +------+------+---------+
            | ram  | 2004 | NULL    |
            | NULL | NULL | NULL    |
            | sam  | 2001 | absent  |
            +------+------+---------+

test_table_2:
            +------+------+---------+
            | name | year | present |
            +------+------+---------+
            | ram  | 2001 | NULL    |
            | sam  | 2002 | present |
            | ramu | 2003 | present |
            | som  | 2004 | absent  |
            +------+------+---------|
'''



## DATABASE  PORTION  FOR   TERM  - II

'''
(I) Database concepts: introduction to database concepts and its need

(II) Relational data model: relation, attribute, tuple, domain, degree, cardinality, keys (candidate key,primary key, alternate key, foreign key)

(III) Structured Query Language: introduction, Data Definition Language and Data Manipulation
Language, data type (char(n), varchar(n), int, float, date), constraints (not null, unique, primary
key), create database, use database, show databases, drop database, show tables, create table,
describe table, alter table (add and remove an attribute, add and remove primary key), drop table,
insert, delete, select, operators (mathematical, relational and logical), aliasing, distinct clause,
where clause, in, between, order by, meaning of null, is null, is not null, like, update command,
delete command


(IV) Aggregate functions (max, min, avg, sum, count), group by, having clause, joins : Cartesian product on two tables, equi-join and natural join

(V) Interface of python with an SQL database: connecting SQL with Python, performing insert, update,
delete queries using cursor, display data by using fetchone(), fetchall(), rowcount, creating
database connectivity applications
'''

