https://t-sibiraj.github.io/sql/                    [Light Mode]()                  [Dark Mode]()  

# DATABASE CONCEPTS:

​                             #  **SKIP TO SQL  IF YOU ALREADY KNOW DATABASE CONCEPTS  #** 

 **EXTENDED READING FOR DATABASE CONCEPTS :**

 https://cbseacademic.nic.in/web_material/doc/cs/2_Computer_Science_Python_ClassXII.pdf



### DATABASE

```sql
Database is a collection of related information that is organized in such a way that it supports for easy access, modification and maintainance data

Examples of database: Ms-Access, MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle, SAP, dBASE, FoxPro, etc..
```



### RELATION:

```sql
In database, a relation means a 'table', in which data are organized in the form of rows and columns.
```



### DOMAIN:

A domain is a **set of acceptable values of a particular column**, which is based on various properties and data types.

| Ad No | Name | Gender | Marital Status |     SUBJECT      |
| :---: | :--: | :----: | :------------: | :--------------: |
|  101  |  A   |  MALE  |   UNMARRIED    |       MATH       |
|  105  |  B   | FEMALE |    MARRIED     |     PHYSICS      |
|  203  |  C   |  MALE  |    DIVORCED    |    CHEMSITRY     |
|  205  |  D   | FEMALE |     WIDOW      | COMPUTER SCIENCE |

For example: 

**(i)** The domain of gender column has a set of two possible values i.e, **Male or Female.** 

**(ii)** The domain of marital status has a set of four possible values i.e, **Married, Unmarried, Widows and Divorced**

** **(iii)** The domain of subject has a **set of five possible** values i.e., **Math's,physics,chemistry,computer science and english**





### TUPLE:

```
Horizontal subset/information in a table is called tuple. The tuple is also known as a 'record', which gives particular information of the relation (table). 

For example: 

(i) In customer table, one row gives information about one customer only. 

(ii) In student table, one row gives information about one student only.
```



### KEY:

Key is of **four types**:

​	**(i) Primary Key**

​	**(ii) Candidate Key**

​	**(iii) Foreign Key**

​	**(iv) Alternate Key**

### **Primary Key:** 

```sql
A column or **set of columns that uniquely identifies a row** within a table is called primary key. 

PRIMARY KEY ---> THIS IS SERVES AS AN UNIQUE INDENTIFIER
		   ---> TWO PERSON CAN HAVE SAME NAME BUT THEY CAN''T HAVE SAME FINGERPRINT
            ---> HERE FINGERPRINT SERVES THE PURPOSE OF PRIMARY KEY
		   ---> IN TABLE WE MUST HAVE A PRIMARY KEY TO UNIQUELY IDENTIFY A RECORDS IN A TABLE 

                   ╔════╦══════╦════════╗              
                   ║ id ║ name ║ gender ║
                   ╠════╬══════╬════════╣
                   ║ 2  ║ sam  ║ male   ║
                   ╠════╬══════╬════════╣
                   ║ 1  ║ ram  ║ female ║
                   ╠════╬══════╬════════╣
                   ║ 3  ║ ram  ║ male   ║
                   ╚════╩══════╩════════╝
                  TABLE NAME: GENDER 

IN THE TABLE GENDER WE CAN SELECT id HAS PRIMARY KEY AS IT ONLY HAS UNIQUE RECORDS. WE CAN''T USE NAME AND GENDER AS PRIMARY KEY AS TWO PERSON CAN HAVE SAME NAME AND TWO PERSON CAN HAVE SAME GENDER
```



### Candidate Key: 

```
Candidate keys are set of fields (columns with unique values) in the relation that are eligible to act as a primary key.

Candidate key  = Collection of Primary key
```

 

### Alternate Key:

 

```
Out of the candidate keys, after selecting a key as primary key, the remaining keys are called alternate key.

Alternate Key =  Candidate key - Primary key
```

 

### Foreign Key:

 A foreign key is a field (or collection of fields) in one table that **uniquely identifies a row of another table**. In other words, a foreign key is a column or a combination of columns that is used to **establish a link between two tables.**

```
#FOREIGN KEY CONSTARINT

#FOREIGN KEY IS LIKE PRIMARY KEY. IT IS USED IN RDBMS.

#SO FAR WE HAVE ONLY SEE DBMS.

DBMS ---> Database Managament System
RDBMS ---> Relational Database Management System

IN RDBMS TABLES ARE IN RELATION WITH EACH OTHER BUT IN DBMS TABLES ARE NOT IN  RELATION WITH EACH OTHER.


DBMS

DATABSSE NAME: RDBMS

╔════╦══════╦══════╗                   ╔════╦══════╦════════╗              
║ id ║ name ║ age  ║                   ║ id ║ name ║ gender ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 1  ║ ram  ║ 10   ║                   ║ 2  ║ sam  ║ male   ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 2  ║ sam  ║ 20   ║                   ║ 1  ║ ram  ║ female ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 3  ║ ram  ║ 30   ║                   ║ 3  ║ ram  ║ male   ║
╚════╩══════╩══════╝                   ╚════╩══════╩════════╝
TABLE NAME: AGE                        TABLE NAME: GENDER 


AS YOU CAN SEE BOTH THE TABELS ARE RELATED TO EACH OTHER BY THE ID COLOUMN

id column in table AGE is called the primary key and id in table GENDER is called primary key

id column is called as the foriegn key as it is used to relate the two tables AGE AND GENDER.
WE can even choose the gender coloumn as the primary key but we can''t choose it as foreign key as it is not present in the age table.


DATABASE DBMS:
╔═══════╦══════╦══════╗                   ╔════╦══════╦════════╗              
║ weight║ name ║ age  ║                   ║ id ║ name ║ gender ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 40    ║ ram  ║ 10   ║                   ║ 2  ║ sam  ║ male   ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 50    ║ sam  ║ male ║                   ║ 1  ║ ram  ║ female ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 60    ║ ram  ║ male ║                   ║ 3  ║ ram  ║ male   ║
╚═══════╩══════╩══════╝                   ╚════╩══════╩════════╝      
TABLE NAME: AGE                            TABLE NAME: GENDER 

TWO TABLES ARE NOT RELATED TO EACH OTHER SO IT IS CALLED AS DBMS
```



## Degree:

```
The number of attributes(fields)(column) in a table

Degree ---> no of columns
```



## Cardinality:

```
The number of tuple(record)(rows) in a table

Cardinality ---> no of rows
```

![‪](images\cbse-keys.jpg)
															SOURCE: cbseacademic.com

```
Candidate Key: AdNo and Name has unique values. 

Primary Key: Out of the AdNo and Name, AdNo is the primary key. 

Alternate Key: In the candidate key, AdNo is the primary key and the Name is the Alternate key. 
```



![https://www.guru99.com/images/1/100518_0517_DBMSKeysPri1.png](https://www.guru99.com/images/1/100518_0517_DBMSKeysPri1.png)

​																SOURCE:www.guru99.com



![](https://powerbidocs.com/wp-content/uploads/2019/12/SQL-Keys.png)

​																	SOURCE: powerbidocs.com

Resources:

```
https://powerbidocs.com/2019/12/25/sql-keys/
```



## Advantages of SQL:

```
(i) SQL is portable

(ii) High Speed

(iii) Easy to learn

(iv)SQL is used with any DBMS system with any vendor: SSQL is used for relational databases: SQL is widely used for relational databases. 

(v)SQL acts as both programming language and interactive language: 

(vi)Client/Server language:

(vii)Supports object based programming
```



## SOME MYSQL SQL ELEMENTS:

## (i) Literals(have fixed value):

```
numeric literal --> 53 ,64

string literal ---> "abc"

real literals ---> 17.0 ,  17.5
```



## (ii) Data Types:

###  (I) Numeric :

### (I) Number:

	Number:
	
	Positive numbers in the range 1 x 10-130 to 9.99...9 x 10125 with up to 38 significant digits.
	
	Negative numbers from -1 x 10-130 to 9.99...99 x 10125 with up to 38 significant digits.
	Zero.
### (II) Decimal/Float:

```
DECIMAL[ (p[ , s] )]` 

– 'p' is the precision or the total number of significant decimal digits, where the most significant digit is the left-most nonzero digit and the least significant digit is the right-most known digit.

– 's' is the scale or the number of digits from the decimal point to the least significant digit.
```



​	**(III) INT/INTERGER**

​    **(IV) FLOAT**

### (ii) CHARACTER OR STRING:

```
CHAR(10) has fixed length, right padded with spaces.
VARCHAR(10) has fixed length, right padded with NULL
VARCHAR2(10) has variable length.

the difference between VARCHAR and VARCHAR2 is that VARCHAR is ANSI standard but takes up space
for variables, whereas the VARCHAR2 is used only in Oracle but makes more efficient use of space.
```

### (III) DAT AND TIME:

```
DATE: YYYY-MM-DD -> 2021-01-01

DATETIME: YYYY-MM-DD HH:MM:SS 2021-01-01 10:10:10

TIME: HH:MM:SS 11:59:10

YEAR: 

-> YEAR(2) -> 2-digit format(21)
-> YEAR(4) -> 4-digit format(2021) 

TIMESTAMP: (YYYYMMDDHHMMSS) --> 20210101060510
```



## TYPES  OF  SQL  STATEMENTS 

### **(i)Data Definition Language **(DDL) statement:

DDL statements are used to **create structure of a table, modify the existing structure of the table and remove the existing table**. Some of the DDL statements are CREATE TABLE, ALTER TABLE and DROP TABLE.

**Grant and revoke privileges and roles and maintenance commands**

### **(ii)** **Data Manipulation Language** (DML) statement:

Data Manipulation Language (DML) statements are used to **access and manipulate data in existing tables.** The manipulation includes **inserting data into tables, deleting data from the tables, retrieving data and modifying the existing data**. The common DML statements are SELECT, UPDATE, DELETE and INSERT.

**(iii) Transaction Control Language(TCL) Commands:**

​	**COMMIT , ROLLBACK , SAVEPOINT , SET TRANSACTION**

**(iv) Session Control Commands**

**(v) System Control Commands**



------



# SQL

(Structured Query Language is a standard language used for accessing databases)

(ALL THE SQL COMMANDS WHICH ARE LISTED BELOW ARE COMPITABLE WITH MySQL

MySQL :https://dev.mysql.com/doc/

SQL Server:https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15)



> - ​              ***SQL IS CASE INSENSITIVE***
>
>   ------
>

Consider 

**Name of the table --> records**

| s.no | student_name |      email       | year | column_name |
| :--: | :----------: | :--------------: | :--: | :---------: |
|  1   |     ram      |  ram@gmail.com   | 2004 |     10      |
|  2   |     sam      |  sam@yahoo.com   | 2003 |     20      |
|  3   |     hari     | hari@outlook.com | 2002 |     30      |

## **TABLE CREATION COMMANDS:**

```
DATATYPES:

char() varchar() integer() decimal() '2001-12-30'
char   varchar   integer   decimal NUMBER()
```



```sql
#TO CREATE A DATABASE

SYNTAX:  CREATE DATABASE database_name;
EXAMPLE: CREATE db;

# IF WE DON'T KNOW WHEATHER A DATABSE EXISTS OR NOT --> WE CAN USE  ---> IF NOT EXISTS

CODE: CREATE DATABASE IF NOT EXISTS db;
/* db database will be created if it not exists */
```
```sql
#TO CREATE A TABLE

SYNTAX:  CREATE TABLE table_name 
		(coloumn_name property, ....);

EXAMPLE: CREATE TABLE records 
	  (sno integer, student_name varchar(10) , email varchar(20), year integer,column_name integer) ;

**NOTE: WE MUST USE A DATABASE BEFORE WE CREATE TABLES AND A TABLE MUST HAVE AT LEAST ONE VISIBLE COLUMN**


```
```sql
#TO ADD A SINGLE RECORD

SYNTAX: INSERT INTO table_name VALUES  (item_name , .....)
NOTE: WE CAN ALSO USE VALUE INTSEAD OF VALUES AS WE ADD A SINGLE RECORDS

EXAMPLE: INSERT INTO records VALUES
    	(1, 'ram', 'ram@gmail.com', 2004, 10)
```
```sql
#TO ADD MULTIPLE REOCRDS

SYNTAX: INSERT INTO table_name VALUE
	    (row_1_item_no_1 , row_1_item_no_2 , row_1_item_no_3)  
	    (row_2_item_no_1 , row_2_item_no_2 , row_2_item_no_2)
	    				....
	    				....
	    (row_n_item_no_1 , row_n_item_no_2 , row_n_item_no_3)				

INSERT INTO records VALUES
    (2, 'sam', 'sam@yahoo.com', 2003, 20),
    (3, 'hari', 'hari@outlook.com', 2002, 30),
    (4, 'ramu', 'ramu@gmail.com', 2004, 20);


```



## SELECT

```sql
#TO SELECT A SINGLE COLUMN

SYNTAX: SELECT column_name
	    FROM table_name;

EXAMPLE: SELECT student_name
		FROM records;
OUTPUT:
        +--------------+
        | student_name |
        +--------------+
        | ram          |
        | sam          |
        | hari         |
        | ramu         |
        +--------------+
```
```sql
#TO SELECT MULTIPLE COLUMN

SYNTAX: SELECT column_name_1,column_name_2,column_name_3
        FROM table_name;

EXAMPLE: SELECT student_name , year;
		FROM records;

OUTPUT: 
        +--------------+------+
        | student_name | year |
        +--------------+------+
        | ram          | 2004 |
        | sam          | 2003 |
        | hari         | 2002 |
        | ramu         | 2004 |
        +--------------+------+
```
```sql
#TO SELECT ALL THE COLUMNS FROM A TABLE:

SYNTAX: SELECT *
        FROM table_name;

EXAMPLE: SELECT * 
		FROM records;

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+	
```


```sql
#TO SELECT ALL THE VALUES FROM A COLUMN WITHOUT ANY DUPLICATES RECORDS

SYNTAX: SELECT DISTINCT column_name
	    FROM table_name;

EXAMPLE: SELECT DISTINCT year
		FROM records;

OUTPUT:
        +------+
        | year |
        +------+
        | 2004 |
        | 2003 |
        | 2002 |
        +------+
```
```SQL
#USING ARITHMETIC OPERATORS

+ , - , * , / , %

#SELF - EXPLANATORY
CODE: SELECT year , year * 100 
	  FROM records;

OUTPUT:
        +------+------------+
        | year | year * 100 |
        +------+------------+
        | 2004 |     200400 |
        | 2003 |     200300 |
        | 2002 |     200200 |
        | 2004 |     200400 |
        +------+------------+
===================================================================================================

CODE: SELECT year ,  year * 10 , "TEST"
	  FROM records;

OUTPUT:
        +------+-----------+------+
        | year | year * 10 | TEST |
        +------+-----------+------+
        | 2004 |     20040 | TEST |
        | 2003 |     20030 | TEST |
        | 2002 |     20020 | TEST |
        | 2004 |     20040 | TEST |
        +------+-----------+------+
===================================================================================================

#SELF-EXPLANATORY
CODE: SELECT 7+1;

OUTPUT:
        +-----+
        | 7+1 |
        +-----+
        |   8 |
        +-----+
===================================================================================================

CODE: SELECT 7 % 2;

OUTPUT:
        +-------+
        | 7 % 2 |
        +-------+
        |     1 |
        +-------+

```



## SHOW  AND  DESCRIBE:

```sql
SYNTAX: SHOW TABLES

Shows the list of tables inside the current database

OUTPUT: 
        +--------------+
        | Tables_in_db |
        +--------------+
        | records      |
        +--------------+
===================================================================================================        
SYNTAX: DESCRIBE table_name or DES table_name;

EXAMPLE: DESCRIBE records

NOTE: WE CAN ALSO USE DES INSTEAD OF DESCRIBE

OUTPUT:
        +--------------+-------------+------+-----+---------+-------+
        | Field        | Type        | Null | Key | Default | Extra |
        +--------------+-------------+------+-----+---------+-------+
        | sno          | int         | YES  |     | NULL    |       |
        | student_name | varchar(10) | YES  |     | NULL    |       |
        | email        | varchar(20) | YES  |     | NULL    |       |
        | year         | int         | YES  |     | NULL    |       |
        | column_name  | int         | YES  |     | NULL    |       |
        +--------------+-------------+------+-----+---------+-------+
```

## ALIASING:

```sql
#USING ALIAS

SYNTAX: SELECT coloumn_name as alias_name  /*USE OF AS IS OPTIONAL */
	    FROM table_name;

EXAMPLE: SELECT year as this_will_display_instead_of_year
		FROM records;

**NOTE: Alias name does not change the actual coloumn name. Orginal coloumn name remains the same**

		
OUTPUT:
        +-----------------------------------+
        | this_will_display_instead_of_year |
        +-----------------------------------+
        |                              2004 |
        |                              2003 |
        |                              2002 |
        |                              2004 |
        +-----------------------------------+
**NOTE: USE OF AS IS OPTIONAL. THE BELOW CODE WILL YIELD TTHE SAME RESULT AS THE ABOVE ONEE.
ALSO THERE SHOULD BE NO SPACE IN BETWEEN IF WE USE ALIAS NAME WITHOUT QUOTES.

SELECT year as y FROM records (OR) SELECT year y FROM records (OR) SELECT year 'y' FROM records
            --------                          ----                             ----
===================================================================================================

#ALIASING MULTIPLE COLOUMN NAMES

SYNTAX: SELECT column_name AS new_name, another_column_name as another_new_name
        FROM table_name;

CODE: SELECT student_name as name , year as ' birth year' 
	  FROM records;
```

### TABLE   ALIASES( PREREQUSITE :      JOINS)

```sql
#TABLE ALIASES

LIKE COLUMN ALIASES WE CAN HAVE ALIAS NAME FOR TABLES TOO

SYNTAX:  SELECT table_alias_1.coloumn_name , table_alias_2
		FROM tabel_name_1 table_alias_1 , table_name_2 table_alias_2;

CONSIDER THE TABLES BELOW

                                	TABLE NAME: records
                +-----+--------------+------------------+------+-------------+
                | sno | student_name | email            | year | column_name |
                +-----+--------------+------------------+------+-------------+
                |   1 | ram          | ram@gmail.com    | 2004 |          10 |
                |   2 | sam          | sam@yahoo.com    | 2003 |          20 |
                |   3 | hari         | hari@outlook.com | 2002 |          30 |
                |   4 | ramu         | ramu@gmail.com   | 2004 |          20 |
                +-----+--------------+------------------+------+-------------+


                                    TABLE NAME: test_table

                                    +------+------+---------+
                                    | name | year | present |
                                    +------+------+---------+
                                    | ram  | 2004 | NULL    |
                                    | NULL | NULL | NULL    |
                                    | sam  | 2001 | absent  |
                                    +------+------+---------+  
 
                                   TABLE NAME: test_table_3
                    +-----+--------------+------------------+---------------+-------------+
                    | sno | student_name | email            | year_of_birth | column_name |
                    +-----+--------------+------------------+---------------+-------------+
                    |   1 | ram          | ram@gmail.com    |          2004 |          10 |
                    |   2 | sam          | sam@yahoo.com    |          2003 |          20 |
                    |   3 | hari         | hari@outlook.com |          2002 |          30 |
                    |   4 | ramu         | ramu@gmail.com   |          2004 |          20 |
                    +-----+--------------+------------------+---------------+-------------+

CODE: SELECT a1.student_name , a2.year_of_birth
	  FROM records a1 , test_table_3 a2;

OUTPUT:
        +--------------+---------------+
        | student_name | year_of_birth |
        +--------------+---------------+
        | ramu         |          2004 |
        | hari         |          2004 |
        | sam          |          2004 |
        | ram          |          2004 |
        | ramu         |          2003 |
        | hari         |          2003 |
        | sam          |          2003 |
        | ram          |          2003 |
        | ramu         |          2002 |
        | hari         |          2002 |
        | sam          |          2002 |
        | ram          |          2002 |
        | ramu         |          2004 |
        | hari         |          2004 |
        | sam          |          2004 |
        | ram          |          2004 |
        +--------------+---------------+

#WE CAN AVOID THE ABIVE SITUATION USING WHERE CLAUSE

CODE: SELECT a1.student_name , a2.year_of_birth
	  FROM records a1 , test_table_3 a2
	  WHERE a1.sno = a2.sno;

OUTPUT:
        +--------------+---------------+
        | student_name | year_of_birth |
        +--------------+---------------+
        | ram          |          2004 |
        | sam          |          2003 |
        | hari         |          2002 |
        | ramu         |          2004 |
        +--------------+---------------+

WE CAN ALSO OTHER CONDITION WITH WHERE CLAUSE
```

## COMMENTS

```sql
#LIKE PYTHON WE CAN USE COMMENTS

/* THIS IS A COMMENT */
```



## WHERE

```sql
#GENERAL SYNTAX

SELECT coloumn_name,
FROM table_name,
WHERE condition;

NOTE: THE FOLLOWING OPERATORS CAN BE USED IN PLACE OF CONDITION
```

### RELATIONAL   OPERATORS

```sql
#USING RELATIONAL OPERATORS


# = (EQUALITY OPERATOR LIKE == IN PYTHON)   

/*  Q: DISPLAY THE RECORDS OF THE STUDENTS WHOSE NAME IS RAM  */

CODE: SELECT *
	  FROM records
      WHERE student_name = 'ram';

OUTPUT:
        +------+--------------+---------------+------+-------------+
        | sno  | student_name | email         | year | column_name |
        +------+--------------+---------------+------+-------------+
        |    1 | ram          | ram@gmail.com | 2004 |          10 |
        +------+--------------+---------------+------+-------------+
================================================================================================

# >(greater than)  , <(lesser than) , >=(greater than or equal to)  , <=(less than or equal to)

/*  Q: DISPLAY THE RECORDS OF THE STUDENT WHOSE BIRTH YEAR IS LESS THAN OR EQUAL TO 2003  */

CODE: SELECT * 
	  FROM records
      WHERE year <= 2003;

OUTPUT:

        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        +------+--------------+------------------+------+-------------+

================================================================================================

# <> or (!== --> NOT VALID IN MYSQL 8.0)

/*  Q: DISPLAY THE RECORDS OF THE STUDENT WHOSE BIRTH YEAR IS NOT EQUAL TO 2003  */

CODE: SELECT * 
	  FROM records
      WHERE year <> 2003;

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+

```

### BETWEEN


```sql
#BETWEEN 

SYNTAX: SELECT *
        FROM table_name
        WHERE column_name BETWEEN lower_limit AND upper_limit;  #inclusive of upper_limit and lower_limit

/*  Q: DISPLAY THE RECORDS OF THE STUDENT WHOSE BIRTH YEAR IS IN THE RANGE OF 2002 TO 2004 */ 


SYNTAX: SELECT *
        FROM records
        WHERE year BETWEEN 2002 AND 2004;  #includes both 18 and 22 

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+

```
### LIKE 

```sql
#LIKE(only text[string] values)      ---> USING WILDCARDS(REGEX)  --> PATTERNS(REGEX)
#'a%' ---> starting with a
#'%a' ---> ending with a
#'%a%' ---> contains a 
#% --> wildcard
#a% --> pattern
```
```sql
/*  SELECT THE NAME OF THE STUDENT [STARTING] WITH THE LETTER R */ 

CODE: SELECT *
	  FROM records
      WHERE student_name LIKE 'r%';

OUTPUT:
        +------+--------------+----------------+------+-------------+
        | sno  | student_name | email          | year | column_name |
        +------+--------------+----------------+------+-------------+
        |    1 | ram          | ram@gmail.com  | 2004 |          10 |
        |    4 | ramu         | ramu@gmail.com | 2004 |          20 |
        +------+--------------+----------------+------+-------------+

#** Note r% --> will select both r and R ** 

'%r%' ---> WILL SELECT ALL THE RECORS CONTAINING THE LETTER r or R -> (CAN BE START OR IN END AND CAN BE IN BETWEEN)

'%r' ---> WILL SELECT ALL THE RECORDS WHICH ENDS WITH LETTER r or R  

Empty set (0.07 sec) ---> DISPLAYED WHEN IT FINDS NO MATCHING RECORDS(
                                                 SELECT * FROM records WHERE student_name LIKE 'r%';)

===================================================================================================

/* Q:  DISPLAY THE RECORDS THE STUDENTS IF THE LENGTH OF THE NAME OF STUDENT IS EXACTLY THREE CHARACTERS */

CODE: SELECT *
	  FROM records
      WHERE student_name LIKE '___';

"___" ---> There are three underscrore(_) inside the quotes(" ") 
	   ---> Three underscrores are used to match any string with exactly three charcaters 
	   ---> Underscore here represents characters( four underscrore matches any sting with exactly 4 characters) 

OUTPUT:
        +------+--------------+---------------+------+-------------+
        | sno  | student_name | email         | year | column_name |
        +------+--------------+---------------+------+-------------+
        |    1 | ram          | ram@gmail.com | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com | 2003 |          20 |
        +------+--------------+---------------+------+-------------+

===================================================================================================

#DIFFERENCE BETWEEN '___' AND '___%'

'___' ---> MATCHES ANY STRING WHICH HAS EXACTLY THREE CHARACTERS

'___%' ---> MATCHES ANY STRING WHICH HAS AT LEAST THREE CHARACTERS

CODE: SELECT *
	  FROM records
      WHERE student_name LIKE '___%';

OUTPUT: 

        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+
```

### IN 

```sql
#IN (MEMBERSHIP)

/*Q:  DISPLAY THE RECORDS OF THE STUDENT IF A STUDENT IS BORN IN THE YEAR 2002 AND 2004 */

CODE: SELECT *
      FROM records
      WHERE year IN (2002,2004);

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+
```
### LOGICAL  OPERATOR

```sql
#LOGICAL OPERATOR (AND  ,  OR)

#AND (BOTH THE STATEMENTNS MUST BE TRUE)

/*  Treat AND as * (LOGICAL MULTIPLICATION)
		 True as 1
		 False as 0
		 
		 True AND True ---> 1 * 1 ---> 1 ---> True
		 True AND False ---> 1 * 0 ---> 0 ---> False
          False AND True ---> 0 * 1 ---> 0 ---> False
          False AND False ---> 0 * 0 ---> 0 ---> False

		 Anything multiplied by zero is zero so if there

	Treat OR as + (LOGICAL ADDITION)
		
		 True OR True ---> 1 + 1 ---> 1 ---> True   /* here 1+1 --> 1 (still True) */
		 True OR False ---> 1 + 0 ---> 1 ---> True
          False OR True ---> 0 + 1 ---> 1 ---> True
          False OR False ---> 0 + 0 ---> 1 ---> False

*/
```



```sql
#AND (BOTH THE STATEMENTNS MUST BE TRUE)
/* Q: DISPLAY THE REOCORDS OF THE STUDENTS IF THEIR NAME STARTS WITH R AND THEIR BIRTH YEAR IS GREATER THAN OR EQUAL TO2003 */

CODE: SELECT *
      FROM records
      WHERE student_name LIKE 'r%' 
      AND year >= 2003;

OUTPUT:
        +------+--------------+----------------+------+-------------+
        | sno  | student_name | email          | year | column_name |
        +------+--------------+----------------+------+-------------+
        |    1 | ram          | ram@gmail.com  | 2004 |          10 |
        |    4 | ramu         | ramu@gmail.com | 2004 |          20 |
        +------+--------------+----------------+------+-------------+

```
```sql
#OR (AT LEAST ONE OF THE STATEMENT SHOULD BE TRUE) 

/* Q: DISPLAY THE REOCORDS OF THE STUDENTS IF THEIR NAME STARTS WITH R OR IF THEIR BIRTH YEAR IS GREATER THAN OR EQUAL TO 2003 */

CODE: SELECT *
      FROM records
      WHERE student_name LIKE 'r%'
      OR year >= 2003;

OUTPUT:
        +------+--------------+----------------+------+-------------+
        | sno  | student_name | email          | year | column_name |
        +------+--------------+----------------+------+-------------+
        |    1 | ram          | ram@gmail.com  | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com  | 2003 |          20 |
        |    4 | ramu         | ramu@gmail.com | 2004 |          20 |
        +------+--------------+----------------+------+-------------+


```
```sql
#SIMILARITY BETWEEN OR AND IN

CODE 1: SELECT *
        FROM records
        WHERE year = 2002 OR year = 2003 OR year 2004;

/* THE ABOVE QUERY CAN ASLO BE WRITTEN USING THE *IN* OPERATOR  */
       
CODE 2: SELECT *
        FROM records
        WHERE year IN (2002 , 2003 , 2004);

```
```sql
#NOT

CODE: SELECT *
      FROM records
      WHERE student_name NOT LIKE '%a'; /* SELECTS ALL THE RECORDS WHOSE NAME DOESN'T START WITH A */

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+
================================================================================================

CODE: SELECT *
      FROM records
	  WHERE year NOT IN (2004,2002) ;  /* SELECTS ALL THE RECORDS EXCEPT 2004 AND 2002 */
	  
OUTPUT:
        +------+--------------+---------------+------+-------------+
        | sno  | student_name | email         | year | column_name |
        +------+--------------+---------------+------+-------------+
        |    2 | sam          | sam@yahoo.com | 2003 |          20 |
        +------+--------------+---------------+------+-------------+	
	  ================================================================================================

CODE: SELECT *
	  FROM records
      WHERE year NOT BETWEEN 2002 AND 2004; /* SELECTS ALL THE RECORD EXCEPT 2002 , 2003 AND 2004 */

OUTPUT:
		Empty set


# NOT LIKE . IS NOT and so on 
```
## ORDER   BY

```sql
# ORDER BY

#TO ORDER THE VALUES OF A COLUMN BASED ON ANOTHER COLUMN

#NOTE : ORDER BY orders the value in ascending(ASC) order by default.

CODE: SELECT *
      FROM records
      ORDER BY year; #ASC ---> ORDER BY year ASC;

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+

=================================================================================================


#To order an COLUMN which has only words(strings to be specific)

CODE: SELECT *
	  FROM records
       ORDER BY student_name; #orders in alphabetcial order in ASC

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        +------+--------------+------------------+------+-------------+
        
=================================================================================================

#To order in descending order

CODE: SELECT *
	  FROM records
      ORDER BY year DESC; #orders DESC

OUTPUT:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        +------+--------------+------------------+------+-------------+
```

## OPERATOR  PRECEDENCE:

```sql
INTERVAL
BINARY, COLLATE
!
- (unary minus), ~ (unary bit inversion)
^
*, /, DIV, %, MOD
-, +
<<, >>
&
|
= (comparison), <=>, >=, >, <=, <, <>, !=, IS, LIKE, REGEXP, IN, MEMBER OF
BETWEEN, CASE, WHEN, THEN, ELSE
NOT
AND, &&
XOR
OR, ||
= (assignment), :=

SOURCE: https://dev.mysql.com/doc/refman/8.0/en/operator-precedence.html
```

## AGGREGATE   FUNCTIONS:

```sql
#AGGREGRATE FUNCTIONS aka GROUP FUNCTIONS aka MULTIPLE ROW FUNCTIONS

SYNTAX: SELECT aggregate_funtion_name(coloumn_name)
	    FROM table_name;

So far we have only seen only one aggregate function(DISTINCT) if I am correct.
From now on we will learn about the other aggregate functions. 

MORE INFO ON AGGREGATE FUNTION CAN BE FOUND AT : https://dev.mysql.com/doc/refman/8.0/en/aggregate-functions.html

YOU CAN ALSO USE ALIAS WITH AGGREGATE FUNTIONS
```




```sql
#MIN ---> RETURNS THE SMALLEST VALUE IN A COLUMN

CODE: SELECT MIN(year)
      FROM records;

OUTPUT:
        +-----------+
        | MIN(year) |
        +-----------+
        |      2002 |
        +-----------+
```
```sql
#AGGREGATE FUNCTIONS--> THOSE WHICH RETURN SINGLE VALUE(MIN,MAX,AVG,SUM,etc..)

#MAX ---> RETURNS THE LARGEST VALUE IN A COLUMN

CODE: SELECT MAX(year)
      FROM records;

OUTPUT:
        +-----------+
        | MAX(year) |
        +-----------+
        |      2004 |
        +-----------+
```
```sql
#AVG ---> TO FIND THE AVERAGE VALUE

average =  value_1 + value_2 + .... value_n
           ---------------------------------
			     no_of_values(n)

CODE: SELECT AVG(year)
      FROM records;

OUTPUT:
        +-----------+
        | AVG(year) |
        +-----------+
        | 2003.2500 |
        +-----------+

average = 2004 + 2003 + 2002 + 2004            =  8013       =  2003.2500 
          ---------------------------             -----
                        4                           4                  
```
```sql
#COUNT --> TO COUNT THE NO ITEMS IN A COLUMN
#IT COUNTS ONLY NON-EMPTY( NULL TO BE SPECIFIC) VALUES  ---> IT DOESN'T TAKE ACCOUNT OF ANY NULL VALUES



CODE: SELECT COUNT(year)
	  FROM records;

OUTPUT:
        +-------------+
        | COUNT(year) |
        +-------------+
        |           4 |
        +-------------+
       ====================================================================================================

#COUNT(*)

#COUNT(*) --> TO COUNT THE NUMBER OF ROWS IN A TABLE

CODE: SELECT COUNT(*)
	  FROM records;

OUTPUT:
        +----------+
        | COUNT(*) |
        +----------+
        |        4 |
        +----------+
===================================================================================================


                  COUNT(coloumn_name) VS COUNT(*)

COUNT(coloumn_name)  ---> ONLY TAKES ACCOUNT OF NON NULL VALUES
COUNT(*)  ----> TAKES ACCOUNT OF NULL AND NON NULL VALUES i.e ALL VALUES


CONSIDER THE TABLE BELOW:

NAME OF THE TABLE: test_table
+------+------+---------+
| name | year | present |
+------+------+---------+
| ram  | 2004 | NULL    |
| NULL | NULL | NULL    |
| sam  | 2001 | absent  |
+------+------+---------+

CODE: SELECT COUNT(present) FROM test_table;
OUTPUT:
        +----------------+
        | COUNT(present) |
        +----------------+
        |              1 |
        +----------------+

CODE: SELECT COUNT(*) FROM test_table;
OUTPUT: 
        +----------+
        | COUNT(*) |
        +----------+
        |        3 |
        +----------+

```
```SQL
#SUM ---> RETURNS THE SUM OF ALL THE VALUES IN A COLUMN

CODE: SELECT SUM(year)
      FROM records;

OUTPUT:
        +-----------+
        | SUM(year) |
        +-----------+
        |      8013 |
        +-----------+
```

```sql
# MORE ON DISTINCT AND ALL

DISTINCT CAN BE USED IN COMBINATION WITH OTHER AGGREGATE FUNCTIONS

MAX( DISTINCT coloumn_name) , MIN( DISTINCT coloumn_name) , AVG( DISTINCT coloumn_name) ,
SUM( DISTINCT coloumn_name) 

WHEN DISTINCT IS USED WITH SUM ONLY DUPLICATE ENTRIES ARE NOT TAKEN INTO ACCOUNT

CODE: SELECT SUM(DISTINCT year)
	  FROM records;

OUTPUT:
        +--------------------+
        | SUM(DISTINCT year) |
        +--------------------+
        |               6009 |
        +--------------------+


#ALL vs DISTINCT VS COUNT---> COSIDER ALL THE VALUES

CONSIDER THE TABLE BELOW

NAME OF THE TABLE: test_table_2

+------+------+---------+
| name | year | present |
+------+------+---------+
| ram  | 2001 | NULL    |
| sam  | 2002 | present |
| ramu | 2003 | present |
| som  | 2004 | absent  |
+------+------+---------+
COUNT(column_name) ---> counts only non NULL values
COUNT(DISTINCT , column_name) ---->  counts only  distinct non NULL values
COUNT(ALL , coloumn_name) ---> counts only non NULL values

CODE: SELECT COUNT(present) FROM test_table_2;

OUTPUT:
        +----------------+
        | COUNT(present) |
        +----------------+
        |              3 |    ----> present , present , absent
        +----------------+

CODE: SELECT COUNT(DISTINCT present) FROM test_table_2; 
OUTPUT:
        +-------------------------+
        | COUNT(DISTINCT present) |
        +-------------------------+
        |                       2 | ---> present , absent
        +-------------------------+
        
        ( present ,absent(duplicate present is not taken into account while counting)

CODE: SELECT COUNT(ALL present) FROM test_table_2;
OUTPUT:
        +--------------------+
        | COUNT(ALL present) |
        +--------------------+
        |                  3 |   -->  present , present , absent
        +--------------------+
```



## MY   SQL   FUNCTIONS

## STRING  FUNTIONS:  

```sql
#CHAR() 

#NOTE: NEWER VERSIONS OF MYSQL INTERPRETS THE BINARY RESULT AS HEXADECIMAL
  
/*  TYPE status IN MYSQL COMMAND LINE CLIENT  */

Connection id:          11
Current database:       db
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_256_GCM_SHA384
Using delimiter:        ;
Server version:         8.0.27 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    utf8mb4
Conn.  characterset:    utf8mb4
TCP port:               3306
Binary data as:         Hexadecimal #THIS IS THE REASON WHY WE GET HEXADECIAML VALUE
Uptime:                 23 hours 35 min 0 sec


#TO SOLVE THIS PROBLEM FOLLOW THE STEPS BELOW THERE ARE TWO WAYS:

WAY 1:
	ONE QUICK FIX TO SOLVE THIS PROBLEM IS TO USE USING ASCII
	i.e..  SELECT CHAR(65 USING ASCII);
	SYNTAX: CHAR(N,... [USING charset_name])

MORE INFO CAN BE FOUND AT:https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_char

WAY 2:

STEP 1: GOTO TO THE FOLDER WHERE THE BIN FOLDER OF MYSQL SEREVER WHICH WILL BE LOCATED INSIDE MYSQL

IF YOU ARE USING WINDOWS 10 -->  C:\Windows\System32\cmd.exe ---> THIS WOULD BE PATH OF THE BIN FOLDER(IN MOST CASES IF NOT LOCATE THE FOLDER BY YOURSELF)

STEP 2: OPEN COMMAND PROMPT AND KEY IN THE BELOW COMMAND
		mysql -u root -p --skip-binary-as-hex

STEP 3: ENTER THE PASSWORD

STEP 4: RUN THE FOLLOWING 
		SELECT CHAR(65)

/* NOTE YOU NEED TO DO THIS STEP EVERY TIME BEFORE YOU USE MYSQL AND MYSQL CLI CAN BE USED DIRECTLY FROM CMD(COMMAND PROMPT) */

MORE INFO CAN BE FOUND AT: https://bugs.mysql.com/bug.php?id=99480

CODE: SELECT CHAR(65 USING ASCII) AS "Alphabet";

OUTPUT:
        +----------+
        | Alphabet |
        +----------+
        | A        |
        +----------+

=====================================================================================================

#CONCAT()

-> IF COLOUMN NAMES ARE USED THE RECORDS GETS CONCATENATED

CODE: SELECT CONCAT(student_name , year) as "NAME AND YEAR"
	  FROM records;

OUTPUT:
        +---------------+
        | NAME AND YEAR |
        +---------------+
        | ram2004       |
        | sam2003       |
        | hari2002      |
        | ramu2004      |
        +---------------+

-> CAN ALSO BE USED TO CONCAT TWO STRINGS
===================================================================================================

CODE: SELECT CONCAT("SIBI" , "RAJ") AS "NAME";

OUTPUT:
        +---------+
        | NAME    |
        +---------+
        | SIBIRAJ |
        +---------+
===================================================================================================

CODE: SELECT "SI" "BI" "RAJ";
	
OUTPUT:
        +---------+
        | SI      |
        +---------+
        | SIBIRAJ |
        +---------+
=================================================================================================	

#LOWER()/LCASE()  ---> https://dev.mysql.com/doc/refman/8.0/en/string-functions.html#function_lcase

CODE: SELECT LOWER("PYTHON");

OUTPUT:
        +-----------------+
        | LOWER("PYTHON") |
        +-----------------+
        | python          |
        +-----------------+
=================================================================================================

#UPPER()/LCASE() 

CODE: SELECT UPPER("python");

OUTPUT:
        +-----------------+
        | UPPER("python") |
        +-----------------+
        | PYTHON          |
        +-----------------+
=================================================================================================

# TRIM ---> REMOVES TRAILING AND LEADING SPACES --> LIKE STRIP()
# LTRIM ---> LIKE LSTRIP()
# RTIRM ---> LIKE RSTIP()


CODE: SELECT TRIM("  AKA STRIP  ");

OUTPUT:
        +-----------------------+
        | TRIM("  AKA STRIP  ") |
        +-----------------------+
        | AKA STRIP             |
        +-----------------------+
=================================================================================================

#SUBSTRING()/SUBSTR()

SUBSTR(given_string,3,4) ---> SELECT 4 CHARACTERS STARING FROM THE INDEX 3

LEFT SIDE INDEX STARTS FROM 0  AND RIGHT SIDE INDEX STARTS FROM -1

CODE: SELECT SUBSTR("0123456789" , 3 , 4) AS SLICING;

OUTPUT:
        +---------+
        | SLICING |
        +---------+
        | 2345    |
        +---------+
```

## NUMERIC  FUNTIONS

```sql
#MOD() ---> RETURNS THE REMAINDER ---> LIKE % IN PYTHON ---> ** REMAINDER(INT PART) ** 

CODE: SELECT MOD(7,2);

OUTPUT: 
          +----------+
          | MOD(7,2) |
          +----------+
          |        1 |
          +----------+
=================================================================================================

#POWER()

CODE: SELECT POWER(2,3);  ---> 2^3 OR 2**3

OUTPUT:
        +------------+
        | POWER(2,3) |
        +------------+
        |          8 |
        +------------+
=================================================================================================

#ROUND() ---> TO ROUND THE EXPRESSION TO THE NUMBER OF DECIMAL POINT

MORE INFO ON ROUNDING CAN BE FOUND AT: 
https://tutorax.com/blogue/en/how-to-round-decimals-rounding-numbers-guide/#:~:text=There%20are%20certain%20rules%20to,9%20round%20the%20number%20up.

CODE: SELECT ROUND(1.26,1);
OUTPUT:
        +---------------+
        | ROUND(1.26,1) |
        +---------------+
        |           1.3 |
        +---------------+

CODE: SELECT ROUND(1.25,1);
OUTPUT:
        +---------------+
        | ROUND(1.25,1) |
        +---------------+
        |           1.3 |
        +---------------+

CODE: SELECT ROUND(1.26,1);
OUTPUT:
        +---------------+
        | ROUND(1.26,1) |
        +---------------+
        |           1.3 |
        +---------------+
=================================================================================================

#SIGN() ---> RETURNS THE SIGN OF THE NUMBER

CODE: SELECT SIGN(-10);
OUTPUT:
        +-----------+
        | SIGN(-10) |
        +-----------+
        |        -1 |
        +-----------+

CODE: SELECT SIGN(10);
OUTPUT:
        +----------+
        | SIGN(10) |
        +----------+
        |        1 |
        +----------+
=================================================================================================

#SQRT()

CODE: SELECT SQRT(4);

OUTPUT:
        +---------+
        | SQRT(4) |
        +---------+
        |       2 |
        +---------+
=================================================================================================

#TRUNCATE() ---> REMOVES(TURNCATES) THE CHARACTERS UPTO TO THE GIVEN DECIMAL PLACES

CODE: SELECT TRUNCATE(123456,3) AS "I WON'T GET TRUNCATED"; ---> ONLY TRUBCATES DECIMAL PLACES

OUTPUT:
        +-----------------------+
        | I WON'T GET TRUNCATED |
        +-----------------------+
        |                123456 |
        +-----------------------+'

CODE: SELECT TRUNCATE(123.456 , 0) AS "MISSING:456";

OUTPUT:  
        +-------------+
        | MISSING:456 |
        +-------------+
        |         123 |
        +-------------+

```

## DATE  AND  TIME  FUNTIONS

```sql
# CURDATE() / CURRENT_DATE() / CURRENT_DATE ---> RETURNS THE CURRENT DATE

CODE: SELECT CURDATE();
OUTPUT:
	    +------------+
        | CURDATE()  |
        +------------+
        | 2022-01-08 |
        +------------+

CODE: SELECT CURDATE() + 1;
OUTPUT:
        +---------------+
        | CURDATE() + 1 |
        +---------------+
        |      20220109 | ---> 2022-01-08 + 1 ---> 20220109
        +---------------+                          ----  --
=================================================================================================


#DATE() ---> USED TO EXTRACT YYYY-MM-DD PART

CODE: SELECT DATE('2001-01-01');
OUTPUT:
        +--------------------+
        | DATE('2001-01-01') |
        +--------------------+
        | 2001-01-01         |
        +--------------------+

CODE: SELECT DATE('2001-01-01 01:01:01');
OUTPUT:
        +-----------------------------+
        | DATE('2001-01-01 01:01:01') |
        +-----------------------------+
        | 2001-01-01                  |
        +-----------------------------+
=================================================================================================

#MONTH() --> USED TO EXTRACT MM PART

CODE: SELECT MONTH('2001-01-01');
OUTPUT:
        +---------------------+
        | MONTH('2001-01-01') |
        +---------------------+
        |                   1 |
        +---------------------+
        =================================================================================================

#YEAR() ---> SELF EXPLANATORY

CODE: SELECT YEAR('2001-01-01');
OUTPUT:
        +--------------------+
        | YEAR('2001-01-01') |
        +--------------------+
        |               2001 |
        +--------------------+
=================================================================================================

#NOW() ---> RETURNS US THE TIME WHEN THE FUNTION STARTED TO GET EXCECUTED

CODE: SELECT NOW();
OUTPUT:
        +---------------------+
        | NOW()               |
        +---------------------+
        | 2000-01-01 01:01:01 |
        +---------------------+
=================================================================================================

#SYSDATE() ---> RETURN US THE CURRENT DATE AND TIME

CODE: SELECT SYSDATE();
OUTPUT:
        +---------------------+
        | SYSDATE()           |
        +---------------------+
        | 2000-01-01 01:01:01 |
        +---------------------+
=================================================================================================

CODE: SELECT NOW() , SLEEP(5) , NOW();
OUTPUT:
        +---------------------+----------+---------------------+
        | NOW()               | SLEEP(5) | NOW()               |
        +---------------------+----------+---------------------+
        | 2000-01-01 01:01:01 |        0 | 2000-01-01 01:01:01 |  ---> SAME TIME
        +---------------------+----------+---------------------+

CODE: SELECT SYSDATE() , SLEEP(5) , SYSDATE();
OUTPUT:
        +---------------------+----------+---------------------+
        | SYSDATE()           | SLEEP(5) | SYSDATE()           |
        +---------------------+----------+---------------------+
        | 2000-01-01 01:01:01 |        0 | 2000-01-01 01:01:06 | ----> INITAL TIME + 5 SECONDS
        +---------------------+----------+---------------------+

CODE: SELECT NOW() , SLEEP(5) , SYSDATE();
OUTPUT:
        +---------------------+----------+---------------------+
        | NOW()               | SLEEP(5) | SYSDATE()           |
        +---------------------+----------+---------------------+
        |  2000-01-01 01:01:01|        0 | 2000-01-01 01:01:06 | ---> INITAL TIME + 5 SECONDS
        +---------------------+----------+---------------------+

CODE: SELECT SYSDATE()  , SLEEP(5) , NOW();
OUTPUT:
        +---------------------+----------+---------------------+
        | SYSDATE()           | SLEEP(5) | NOW()               |
        +---------------------+----------+---------------------+
        | 2000-01-01 01:01:01|        0 | 2000-01-01 01:01:01 |  ---> SAME TIME
        +---------------------+----------+---------------------+
```

## Null  Handling

```sql
Let us consider the tabel given below:

NAME OF THR TABLE: records3
+------+------+---------+
| name | year | present |
+------+------+---------+
| ram  | 2001 | present |
| sam  | 2002 | present |
| ramu | 2003 | NULL    |
+------+------+---------+

To create the table above use the following commands:
USE db;  ---> (use database_name)
CREATE TABLE records3(name varchar(10) , year integer , present varchar(10));
INSERT INTO records3 VALUES('ram' , 2001 , 'present') , ('sam' , 2002 , 'present'), ('ramu', 2003 , NULL);


NULL here in the present coloumn means that the person is absent on that particular day(2001-01-01).
The day we are here refereing to is 2001-01-01.

#IFNULL()

Syntax: IFNULL(coloumn_name , value_to_be_substitued)

IFNULL() ---> Used to change all the NULL value from the give coloumn to the given value

CODE: SELECT name , year , IFNULL(present , 'absent')
	  FROM records3;

OUTPUT:
        +------+------+----------------------------+
        | name | year | IFNULL(present , 'absent') |
        +------+------+----------------------------+
        | ram  | 2001 | present                    |
        | sam  | 2002 | present                    |  ---> NULL values are changed into absent
        | ramu | 2003 | absent                     |
        +------+------+----------------------------+

===================================================================================================

#USING **AS** WITH IFNULL()

CODE: SELECT name , year , IFNULL(present , ' absent') AS 'attendance'
	  FROM records3;

OUTPUT:
        +------+------+------------+
        | name | year | attendance |
        +------+------+------------+
        | ram  | 2001 | present    |
        | sam  | 2002 | present    |
        | ramu | 2003 |  absent    |
        +------+------+------------+
===================================================================================================

#FINDING NULL USING THE WHERE OPERATOR:

CODE: SELECT * 
	  FROM records3
	  WHERE present IS NULL;  ---> SELECTS ALL THE NULL VALUE

OUTPUT:
        +------+------+---------+
        | name | year | present |
        +------+------+---------+
        | ramu | 2003 | NULL    |
        +------+------+---------+

CODE: SELECT * 
	  FROM records3
	  WHERE present IS NOT NULL;  ---> SELF - EXPLANATORY

OUTPUT:
        +------+------+---------+
        | name | year | present |
        +------+------+---------+
        | ram  | 2001 | present |
        | sam  | 2002 | present |
        +------+------+---------+
```

## MISSED    NUANCES

```sql
/* In this section we will cover a few nuances that we have missed earlier */

SELECT year  (or) SeLeCt year    (or)  sELEcT yEar 
FROM records; (or) fRoM records; (or)  fROm rECROds; 

ALL THE ABOVE QUERIES YIELD THE SAME RESULT ---> SQL IS CASE INSENSTIVE
===================================================================================================

NUMBER()

NUMBER(5,3) ---> NUMBER WITH A MAXIMUM OF 5 DIGIT WITH 3 DECIMAL PLACES
===================================================================================================

STRING VS NUMERIC FUNTIONS

THE OUTPUT OF ALL THE STRING FUNCTIONS STARTS FROM THE LEFT

THE OUTPUT OF ALL THE NUMERIC FUNTIONS STARTS FROMT THE RIGHT

	    NUMERIC FUNTION                     STRING FUNCTION
    
        +-------------+
        | MISSING:456 |                     +-----------------+
        +-------------+                     | LOWER("PYTHON") |
        |          123|                     +-----------------+
        +-------------+                     | python          |
                                            +-----------------+

===================================================================================================

SUBSTR(given_string , start_index ,  no_of_characters)

start_index ---> can be negative or positive (POSITIVE OR NEGATIVE NUMBERS)
no_of_character ---> must be a positive integer(NATURAL NUMBERS)

CODE: SELECT SUBSTR('0123456789' , 3 , -4);
OUTPUT: 
        +-------------------------------+
        | SUBSTR('0123456789' , 3 , -4) |
        +-------------------------------+
        |                               |
        +-------------------------------+
===================================================================================================

USING ARITHEMTIC AND RELATIONAL OPERATOR WITH DATE AND TIME FUNTIONS

CODE: SELECT YEAR('2001-01-01') + 10;
OUTPUT:        
        +-------------------------+
        | YEAR('2001-01-01') + 10 |
        +-------------------------+
        |                    2011 |
        +-------------------------+   
===================================================================================================

CODE: SELECT YEAR('2001-01-01') > 10;
OUTPUT: 
        +-------------------------+
        | YEAR('2001-01-01') > 10 |
        +-------------------------+
        |                       1 |  --> 1 --> True
        +-------------------------+
```

## TABLES   USED

```sql
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
```

## TABLE   CREATION   COMMANDS  (CONTINUED)

## DROP

```sql
#TO DELETE A DATABASE

SYNTAX: DROP DATABASE database_name;
EXAMPLE: DROP DATABASE db;    #---> Database db will be deleted if it exists
OUTPUT: Query OK, 0 rows affected (0.31 sec)

#TO DELETE A TABLE

SYNTAX: DROP table_name;
EXAMPLE: DROP records;  #---> Table records will be deleted if it exists
OUTPUT: Query OK, 0 rows affected (1.15 sec)

#TO DELETE A COLUMN

SYNTAX: ALTER TABLE table_name
	    DROP COLUMN column_name;
EXAMPLE: ALTER TABLE records
		DROP COLUMN year;   # column  year will be deleted

#IF EXISTS

CAN BE USED TO DELTE A TABLE IF IT EXISTS

SYNTAX: DROP TABLE IF EXISTS table_name;
SYNAX: DROP TABLE IF EXISTS records; #---> Table records will be deleted if it exists
```

## CONSTRAINT

```sql
#CONSTRAINT

DATABASE INTERGRITY CONSTRAINTS:
(i)   Unique constraint
(ii)  Primary Key constraint
(iii) Foreign Key constraint
(iv)  CHeck constraint
(v)   Default Key constraint
(vi)  NOT NULL
(vii) ENUM
(Vii) SET
and so on...
===========================================================================================

#NOT NULL  ---> SHOULD BE USED WHEN YOU DON'T WANT AN COLOUMN TO ACCEPT NULL DATA

CODE:  CREATE TABLE records4
	  (sno integer,
       student_name varchar(10) 
       ,email varchar(20) NOT NULL) ;
/* email column now can't accept NOT NULL values*/

CODE:   INSERT INTO records4 VALUE(1,'ram',NULL);
OUTPUT: ERROR 1048 (23000): Column 'email' cannot be null
===========================================================================================

#UNIQUE ---> SHOULD BE USED WHEN YOU DON'T WANT A COLOUMN TO HAVE UNIQUE RECORDS(NO DUPLICATE RECORDS)

CODE: CREATE TABLE records6 
      ( sno           integer     NOT NULL UNIQUE, 
        student_name  varchar(10) , 
        email         varchar(20) NOT NULL) ;

CODE: INSERT INTO records6 VALUE
	 (1,'ram','ram@gmail.com');
OUTPUT:	Query OK, 1 row affected 

CODE: INSERT INTO records6 VALUE
	(1,'ram','ram@yahoo.com');

OUTPUT: ERROR 1062 (23000): Duplicate entry '1' for key 'records6.sno'
===========================================================================================

#PRIMARY KEY  ---> CAN BE APPPLIED TO ONLY ONE COLOUMN AND IT DOESN'T ALLOW NULL VALUES
				# ERROR(ERROR 1068 (42000): Multiple primary key defined) ---> PRODUCED WHEN APLIIED 				  TO MULTIPLE COLUMNS

PRIMARY KEY ---> THIS IS SERVES AS AN UNIQUE INDENTIFIER
		   ---> TWO PERSON CAN HAVE SAME NAME BUT THEY CAN''T HAVE SAME FINGERPRINT
            ---> HERE FINGERPRINT SERVES THE PURPOSE OF PRIMARY KEY
		   ---> IN TABLE WE MUST HAVE A PRIMARY KEY TO UNIQUELY IDENTIFY A RECORDS IN A TABLE 

AS WE KNOW PRIMARY KEY DOES NOT ALLOW NULL VALUES THE PRIMARY KEY ALSO ACTS LIKE NOT NULL CONSTARINT

CODE: CREATE TABLE records7
	 (name NOT NULL PRIMARY KEY);    ---> NOT NULL MAY OR MAY NOT BE USED WITH PRIMARY KEY

			(OR)
			
CREATE TABLE records7
	 (name PRIMARY KEY); #PRIMARY KEY ALSO ACTS LIKE NOT NULL
=================================================================================================

#DEFAULT CONSTRAINT

CODE: CREATE TABLE records8(name DEFAULT 'I AM')
      
      INSERT INTO records8 VALUE();
  
  /* IN THIS CASE THE DEFAULT VALUE 'I AM' WILL BE ADDED */

	 SELECT * FROM records8;

OUTPUT:
        +------+
        | name |
        +------+
        | I AM |
        +------+

NOTE: THE MAX SIZE OF DEFAULT VALUE IS 10;
# AS WE DID NOT INCLUDE ANY VALUE WHILE ADDING RECORDS THE DEFAULT VALUE 'I AM' WAS INSERTED
=================================================================================================

#CHECK CONSTRAINT---> CAN BE USED WHEN YOU WANT TO ALLOW CONSTRAINTS BASED ON CERTAIN LIMIT

CODE:  CREATE TABLE records9 VALUE
	  (name  varchar(10) ,
       age    integer     CHECK(age > 18) ) #IT ONLY ALLOWS VALUES GREATER THAN 18 IN THE age COLUMN


CHECK(column_1 < column_2) ---> CAN BE USED TO COMPARE TWO coloumns

name varchar(10)  CHECK(name in ('ram' , 'som' ,'ramu'))

BETWEEN , LOGICAL OPERATOR AND OTHER OPERATORS CAN BE USED.
===================================================================================================

#FOREIGN KEY CONSTARINT

#FOREIGN KEY IS LIKE PRIMARY KEY. IT IS USED IN RDBMS.

#SO FAR WE HAVE ONLY SEE DBMS.

DBMS ---> Database Managament System
RDBMS ---> Relational Database Management System

IN RDBMS TABLES ARE IN RELATION WITH EACH OTHER BUT IN DBMS TABLES ARE NOT IN  RELATION WITH EACH OTHER.


DBMS

DATABSSE NAME: RDBMS

╔════╦══════╦══════╗                   ╔════╦══════╦════════╗              
║ id ║ name ║ age  ║                   ║ id ║ name ║ gender ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 1  ║ ram  ║ 10   ║                   ║ 2  ║ sam  ║ male   ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 2  ║ sam  ║ 20   ║                   ║ 1  ║ ram  ║ female ║
╠════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 3  ║ ram  ║ 30   ║                   ║ 3  ║ ram  ║ male   ║
╚════╩══════╩══════╝                   ╚════╩══════╩════════╝
TABLE NAME: AGE                        TABLE NAME: GENDER 


AS YOU CAN SEE BOTH THE TABELS ARE RELATED TO EACH OTHER BY THE ID COLOUMN

id column in table AGE is called the primary key and id in table GENDER is called primary key

id column is called as the foriegn key as it is used to relate the two tables AGE AND GENDER.
WE can even choose the gender coloumn as the primary key but we can''t choose it as foreign key as it is not present in the age table.


DATABASE DBMS:
╔═══════╦══════╦══════╗                   ╔════╦══════╦════════╗              
║ weight║ name ║ age  ║                   ║ id ║ name ║ gender ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 40    ║ ram  ║ 10   ║                   ║ 2  ║ sam  ║ male   ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 50    ║ sam  ║ male ║                   ║ 1  ║ ram  ║ female ║
╠═══════╬══════╬══════╣                   ╠════╬══════╬════════╣
║ 60    ║ ram  ║ male ║                   ║ 3  ║ ram  ║ male   ║
╚═══════╩══════╩══════╝                   ╚════╩══════╩════════╝      
TABLE NAME: AGE                            TABLE NAME: GENDER 

TWO TABLES ARE NOT RELATED TO EACH OTHER SO IT IS CALLED AS DBMS
```

### TABLE   CONSTRAINTS

```sql
#TABLE CONSTRAINTS ---> CONSTRAINT APPLIED TO MULTIPLE COLUMNS

CODE: CREATE TABLE t1
	(age  integer,
     name  VARCHAR(10) NOT NULL,
     email VARCHAR(20) NOT NULL
     UNIQUE(name , email));   #UNIQUE CONTRAINT WILL BE APLLIED TO name and email column
```

### NAMED    CONSTRAINTS

```sql
#ASSIGNING NAME TO CONSTRAINTS

MySQL my default assigns name to constarints in the format SYS_Cn , where n is an integer
For eg: SYS_C123456 , SYS_C654321

But we can force change the name of the constraint

SYNTAX: CONSTRAINT the_name_you_want constraint_name;
CODE:  CREATE TABLE students (
       id INTEGER CONSTRAINT new_name PRIMARY KEY,
       NAME varchar(15)
       );

#DEFAULT NAME OF PRIMARY KEY CONSTRAINT HAS BEEN CHANGED TO new_name
#
```

### TABLE   CREATION  FROM    EXISITNG   TABLE

```sql
#CREATING TABLE FROM EXISTSING TABLE

#METHOD 1:(INSERT AND SELECT)

#table_2 should be created earlier
#column datatype and count in records should match column datatype  in table_2
CODE: INSERT INTO table_2
	  SELECT student_name FROM records; #RECORDS IN records ---> COPIED TO TABLE_2

#METHOD 2:(AS SELECT)

CODE: CREATE TABLE T2 AS 
	  SELECT student_name , year FROM records;   #USE OF AS IS OPTIONAL

+--------------+------+
| student_name | year |
+--------------+------+
| ram          | 2004 |
| sam          | 2003 |
| hari         | 2002 |
| ramu         | 2004 |
+--------------+------+

THE ABOVE RECORDS WILL BE STORED IN BOTH THE CASE
	
```

## UPDATE

```sql
SYNTAX: UPDATE table_name
	    SET column_name = value;
```

```sql
#TO UPDATE ALL THE RECORDS IN A COLUMN

CODE: UPDATE records
	  SET year = 2000;    

TABLE:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2000 |          10 |
        |    2 | sam          | sam@yahoo.com    | 2000 |          20 |
        |    3 | hari         | hari@outlook.com | 2000 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2000 |          20 |
        +------+--------------+------------------+------+-------------+

```

```sql
#TO UPDATE A PARTICULAR RECORD

WE CAN USE WHERE TO ACHIEVE THIS TASK

CODE: UPDATE records
	  SET year = 2000
	  WHERE student_name = "ram";

TABLE:
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    1 | ram          | ram@gmail.com    | 2000 |          10 | #2004 TO 2000
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+

SET column_name = 2000 + value  #USING EXPRESSION
```

## DELETE   VS   TRUNCATE(ROW  OPERATION)

```sql
# BOTH DELETE AND TRUNCATE ARE USED TO DELETE ROWS AND ROWS , COLOUMNS RESPECTIVELY BUT THE TABLE NAME STILL EXIST
#BUT DROP IS USED TO DELETE THE TABLE COMPLETELY [TABLE_NAME + ALL THE ROWS AND COLUMNS] OR A PARTICULAR COLUMN
============================================================================================

#TO DELETE ALL THE ROWS FROM A TABLE USING DELETE

SYNTAX: DELETE FROM tabel_name;
CODE:   DELETE FROM records;
OUTPUT: Query OK, 0 rows affected (1.57 sec)
TABLE: Empty set (0.00 sec)
#THE ABOVE CODE DELETES ALL THE ROWS AND COLUMNS BUT THE TABLE IS STILL THERE
================================================================================================


#TO DELETE ALL THE ROWS FROM A TABLE USING TRUNCATE

SYNTAX: TRUNCATE table_name;
CODE:   TRUNCATE records;
OUTPUT: Query OK, 0 rows affected (1.12 sec)
TABLE: Empty set (0.00 sec)
#THE ABOVE CODE DELETES ALL THE ROWS AND COLUMNS BUT THE TABLE IS STILL THERE
================================================================================================


#TO DELETE A PARTICULAR ROW FROM A TABLE USING DELETE

SYNTAX: DELETE FROM table_name
	    WHERE condition

CODE: DELETE FROM records
	  WHERE name = 'ram'; 
TABLE: 
        +------+--------------+------------------+------+-------------+
        | sno  | student_name | email            | year | column_name |
        +------+--------------+------------------+------+-------------+
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +------+--------------+------------------+------+-------------+
        ================================================================================================

#TO DELETE A PARTICULAR ROW FROM A TABLE USING TRUNCATE

WE CAN'' DO THAT USING TRUNCATE

                                    DELETE VS TRUNCATE
```

![image-20220113005614894](images\image-20220113005614894.png)

​																		SOURCE: t-sibiraj.github.io/sql

## ROLLBACK   (COMING SOON)

```sql
THE FOLLOWING CONCEPT IS (/*OUT OF SYLLABUS */)

OUT OF SYLLABUS    ------      OUT OF SYLLABUS   ------  OUT OF SYLLABUS  ---- OUT OF SYLLABUS -----

#TRANSACTION LOG

CODE: BEGIN TRANSACTION 

OUT OF SYLLABUS    ------      OUT OF SYLLABUS   ------  OUT OF SYLLABUS  ---- OUT OF SYLLABUS -----
```

## ALTER  

```sql
SYNTAX: ALTER TABLE table_name
	    clause_name name
```

### ADD

```sql
#TO ADD A COLUMN

SYNTAX: ALTER TABLE table_name
	    ADD coloumn_name datatype(size) CONSTRAINT constraint_name;  size and constarint --> optional

CODE:   ALTER TABLE records
	    ADD (result integer);  #USE OF () IS OPTIONAL WHILE ADDING SINGLE COLUMN

TABLE:
        +------+--------------+------------------+------+-------------+--------+
        | sno  | student_name | email            | year | column_name | result |
        +------+--------------+------------------+------+-------------+--------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |   NULL |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |   NULL |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |   NULL |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |   NULL |
        +------+--------------+------------------+------+-------------+--------+
         ================================================================================================

#TO ADD MULTIPLE COLUMN

CODE: ALTER TABLE records
	 ADD (maths integer , computer_science integer);

TABLE:
+------+--------------+------------------+------+-------------+--------+-------+------------------+
| sno  | student_name | email            | year | column_name | result | maths | computer_science |
+------+--------------+------------------+------+-------------+--------+-------+------------------+
|    1 | ram          | ram@gmail.com    | 2004 |          10 |   NULL |  NULL |             NULL |
|    2 | sam          | sam@yahoo.com    | 2003 |          20 |   NULL |  NULL |             NULL |
|    3 | hari         | hari@outlook.com | 2002 |          30 |   NULL |  NULL |             NULL |
|    4 | ramu         | ramu@gmail.com   | 2004 |          20 |   NULL |  NULL |             NULL |
+------+--------------+------------------+------+-------------+--------+-------+------------------+
===================================================================================================


#TO ADD A COLUMN WITH A CONSTRAINT

CODE: ALTER TABLE records
	  ADD (physics integer NOT NULL);

WE HAVE DELETED ALL THE COLUMNS WHICH HAS NULL VALUE BEFORE ADDING PHYSICS COLUMN

TABLE:
        +------+--------------+------------------+------+-------------+---------+
        | sno  | student_name | email            | year | column_name | physics |
        +------+--------------+------------------+------+-------------+---------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 |       0 |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 |       0 |
        |    3 | hari         | hari@outlook.com | 2002 |          30 |       0 |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 |       0 |
        +------+--------------+------------------+------+-------------+---------+
#0 IS ADDED BY DEFAULT AS WE HAVE ADDED NOT NULL CONSTARINT
```

### CHANGE

```
SYNTAX: ALTER TABLE table_name 
	    CHANGE name
CHANGE:
---> Can rename a column and change its definition, or both.
```

```sql
#TO CHANGE THE COLUMN NAME

SYNTAX: ALTER TABLE table_name
	    CHANGE old_column_name new_column_name datatype(size) CONSTRAINT constraint_name;

CODE: ALTER TABLE records
	  CHANGE physics description varchar(250);

TABLE:
        +------+--------------+------------------+------+-------------+-------------+
        | sno  | student_name | email            | year | column_name | description |
        +------+--------------+------------------+------+-------------+-------------+
        |    1 | ram          | ram@gmail.com    | 2004 |          10 | 0           |
        |    2 | sam          | sam@yahoo.com    | 2003 |          20 | 0           |
        |    3 | hari         | hari@outlook.com | 2002 |          30 | 0           |
        |    4 | ramu         | ramu@gmail.com   | 2004 |          20 | 0           |
        +------+--------------+------------------+------+-------------+-------------+
```

### MODIFY

```sql
MODIFY:
---> Can change a column definition but not its name.

#TO CHANGE THE COLUMNS DATATYPE

SYNTAX: ALTER TABLE table_name 
		MODIFY column_name datatype(size);
		
CODE: ALTER TABLE records
	    MODIFY description varchar(50); #THE DATATYPE CHANGES FROM varchar(250) TO varchar(50)

TABLE:
        +--------------+-------------+------+-----+---------+-------+
        | Field        | Type        | Null | Key | Default | Extra |
        +--------------+-------------+------+-----+---------+-------+
        | sno          | int         | YES  |     | NULL    |       |
        | student_name | varchar(10) | YES  |     | NULL    |       |
        | email        | varchar(20) | YES  |     | NULL    |       |
        | year         | int         | YES  |     | NULL    |       |
        | column_name  | int         | YES  |     | NULL    |       |
        | description  | varchar(50) | YES  |     | NULL    |       |
        +--------------+-------------+------+-----+---------+-------+

===================================================================================================

#TO CHANGE THE ORDER OF THE COLUMN

SYNTAX: ALTER TABLE table_name 
	    MODIFY coloumn_name datatype(size)  FIRST ...;

SYNTAX: ALTER TABLE records 
	    MODIFY description varchar(50) FIRST;
	    
```

### ADD

```sql
#TO ADD A CONSTRAINT

SYNTAX: ALTER TABLE table_name
	    ADD constraint_name(column_name);

CODE:   ALTER TABLE records
	    ADD PRIMARY KEY(sno);    #sno column ---> will be treated as primary key

TABLE:
        +--------------+-------------+------+-----+---------+-------+
        | Field        | Type        | Null | Key | Default | Extra |
        +--------------+-------------+------+-----+---------+-------+
        | description  | varchar(50) | YES  |     | NULL    |       |
        | sno          | int         | NO   | PRI | NULL    |       |
        | student_name | varchar(10) | YES  |     | NULL    |       |
        | email        | varchar(20) | YES  |     | NULL    |       |
        | year         | int         | YES  |     | NULL    |       |
        | column_name  | int         | YES  |     | NULL    |       |
        +--------------+-------------+------+-----+---------+-------+

```

### DROP

```sql
#TO REMOVE A COLUMN

SYNTAX: ALTER TABLE table_name
	    DROP column_name;

CODE: ALTER TABLE records
	  DROP description; #description column ---> deleted

TABLE:
        +-----+--------------+------------------+------+-------------+
        | sno | student_name | email            | year | column_name |
        +-----+--------------+------------------+------+-------------+
        |   1 | ram          | ram@gmail.com    | 2004 |          10 |
        |   2 | sam          | sam@yahoo.com    | 2003 |          20 |
        |   3 | hari         | hari@outlook.com | 2002 |          30 |
        |   4 | ramu         | ramu@gmail.com   | 2004 |          20 |
        +-----+--------------+------------------+------+-------------+
===================================================================================================

#TO REMOVE THE PRIMARY KEY

SYNTAX: ALTER TABLE table_name
	    DROP PRIMARY KEY;

CODE: ALTER TABLE records
	  DROP PRIMARY KEY; #sno will no longer be primary key

TABLE:
        +--------------+-------------+------+-----+---------+-------+
        | Field        | Type        | Null | Key | Default | Extra |
        +--------------+-------------+------+-----+---------+-------+
        | sno          | int         | NO   |     | NULL    |       |
        | student_name | varchar(10) | YES  |     | NULL    |       |
        | email        | varchar(20) | YES  |     | NULL    |       |
        | year         | int         | YES  |     | NULL    |       |
        | column_name  | int         | YES  |     | NULL    |       |
        +--------------+-------------+------+-----+---------+-------+
===================================================================================================


#TO REMOVE THE FOREIGH KEY 

SYNTAX: ALTER TABLE table_name
	    DROP constraint_name column_name;

CODE: ALTER TABLE records
	  DROP FOREIGN KEY email; #email will no longer be foreign key

===================================================================================================


#CASCADE

CODE:  ALTER TABLE table_name
	   DROP PRIMARY KEY CASCADE;

#When we use CASCADE it removes(drops) any foreign key which references the primary key
```

## GROUP   BY(COMING SOON)

```

```

## JOINS

```sql
WE CAN ALSO ACCESS COLUMNS BY USING THE BELOW FORMAT

table_name.column_name   ----> .(dot)
alias_table_name.column_name ----> .(dot)

column_name
alias_column_name

JOIN ---> JOIN is nothing but a query which can be used to combine rows from two or more tables
```

### CARTESIAN    PRODUCT

```sql
LET US CONSIDER THE TABLES BELOW

								  TABLE NAME: records
                +-----+--------------+------------------+------+-------------+
                | sno | student_name | email            | year | column_name |
                +-----+--------------+------------------+------+-------------+
                |   1 | ram          | ram@gmail.com    | 2004 |          10 |
                |   2 | sam          | sam@yahoo.com    | 2003 |          20 |
                |   3 | hari         | hari@outlook.com | 2002 |          30 |
                |   4 | ramu         | ramu@gmail.com   | 2004 |          20 |
                +-----+--------------+------------------+------+-------------+


                                    TABLE NAME: test_table

                                    +------+------+---------+
                                    | name | year | present |
                                    +------+------+---------+
                                    | ram  | 2004 | NULL    |
                                    | NULL | NULL | NULL    |
                                    | sam  | 2001 | absent  |
                                    +------+------+---------+  

CARTESIAN PRODUCT IS NOTHING BUT UNSRESTRICTED JOIN

TABLE STRUCTURE OF records:                            TABLE STRUCTURE OF test_table
 
records                                                test_table
|												   |
|_____ sno										    |_____ name
|												   |
|_____ student_name 							     |_____ year
|												   |
|_____ email									    |_____ present
|
|_____ year
|
|_____ column_name

In SQL we can write the Cartesian product of records and test_table as follows

CODE: SELECT * 
	  FROM records, test_table

#Now the a total 15 records will be shown (5 * 3)
#Each row in records table will be multiplied with all the row from test_table
```

![image-20220113030716529](images\image-20220113030716529.png)

​																		SOURCE: t-sibiraj.github.io/sql

```sql
AS you can see the row  1,ram,ram@gmail.com,2004 from table records
is multplied with all the rows of the table test_table which is colour coded in blue  

A MORE SIMPLE VERSION IS GIVEN BELOW

CODE: SELECT student_name , present
	 FROM records , test_table;

----> student_name [cartesian product] present
```

![image-20220113031336907](images\image-20220113031336907.png)

​																	SOURCE: t-sibiraj.github.io/sql

```
As you can see above row ram is multiplied with all the three rows pressent in the **present column**. And the same is repeated with sam , hari and ramu row.

ram *  ( absent + NULL + NULL)
sam * (absent + NULL + NULL)
hari * (absent + NULL + NULL)
ramu * (absent + NULL + NULL)

THE ORDER WOULD HAVE BEEN CHANGED IF THE COLUMN present WAS WRITTEN BEFRORE THE name column.
```

### EQUI  -  JOIN

```sql
#EQUI - JOIN 

--> Columns are compared for equality
--> Duplicate columns are not eliminated
```

## PIP

```sql
SIMPLE DEFINTION:

Think of ***PyPI** as a place where people upload their **python libraries and modules**
Like a **website** where people upload **education material**

We can use the **pip** to install the **libraries** uploaded by the people on PyPI in our computer
We can use our **browser** to download the **education material** uploaded by others on the website in our computer

FORMAL DEFINITON:
The Python Package Index (PyPI) is a repository of software for the Python programming language.
(source: https://pypi.org/)

repository: storage location for software packages

PIP is nothing but a package managament system. It is used to download libraries , modules created by other people  which they have uploaded to PyPI.
```

![image-20220113034025814](images\image-20220113034025814.png)

​																				SOURCE: pypi.org     

​																			PyPI website homepage

```SQL
#STEPS TO INSTALL PYTHON LIBRARIES FROM PyPI IN WINDOWS:

1. OPEN CMD WITH ADMINISTER PRIVILLEDGE
2. TO CHECK IF PIP IS INSTALLED TYPE EITHER pip or pip3    #either should work

3. TYPE pip install name_of_the_package or pip3 install name_of_the_package


#WE NEED mysql-connector-python and pymysql libraries to work the sql from python

4.pip install mysql-connector-python
5.pip install pymysql

```



## DATABASE  PORTION  FOR   TERM  - II

```
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
```



- [x] PYTHON 

- [x] NETWORKING 

- [x] SQL

