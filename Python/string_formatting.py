Before we learn about parameterised queries we must know what string formatting is.

#NEW WAY TO FORMAT STRINGS

"{}".format() --> Value inside the bracket gets substituted in the set bracket
			 --> The set brackets are called as placeholders



>>>details = "My name is {} and I am {} years old".format("ram" , 20)
>>>print(details)
My name is ram and I am 20 years old
#ram goes into the first set bracket and 20 into the second

>>>details = "My name is {} and I am {} years old".format(20,"ram")
>>>print(details)
My name is 20 and I am ram years old
#20 goes into the first set bracket and ram into the second
===================================================================================================


>>>details = "My name is {0} and I am {1} years old".format("ram" , 20)
>>>print(details)
My name is ram and I am 20 years old
#ram is in zeroth index and 20 is in 1st index

>>>details = "My name is {1} and I am {0} years old".format(20,"ram")
>>>print(details)
My name is 20 and I am ram years old
'''ram is in zeroth index and 20 is in 1st index. As we have used 1st index first , the value in the 1st index ("ram") gets substituted in the set bracket'''
===================================================================================================


>>>details = "My name is {name} and I am {age} years old".format(age = 20,name = "ram")
>>>print(details)
My name is ram and I am 20 years old
#now we have named the placeholder values as name and age.

===================================================================================================


Example:
    #Write a program in python where you should get year from the user and display the details of the that student whose year is greater than the given year. The details of the students are stored in a database
  
CODE:
    import mysql.connector as connector
    connection = connector.connect(host="localhost",  user="root", passwd  = "root", database = "db")
    cursor = connection.cursor()
    year = input("Enter the year:")
    cursor.execute("SELECT * FROM records WHERE year > {}".format(year))
    print(cursor.fetchall())
    connector.close()
OUTPUT:
    Enter the year:2003
    [(1, 'ram', 'ram@gmail.com', 2004, 10), (4, 'ramu', 'ramu@gmail.com', 2004, 20)]

#OLD WAY TO FORMAT STRINGS 

#This type of formating is used in C language

%s  ---> To be used with string (can also be used with numbers)
%d  ---> To be used with integers
%f  ---> To use used with float 

%char acts like {}

CODE:
	name = "ram"
	age = 20
	print("My name is %s and I am %d years old." % (name, age))

OUTPUT:
	   My name is ram and I am 20 years old
