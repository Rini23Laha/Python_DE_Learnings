# Python_DE_Learnings

What is Python  --> Python is high level interpreted programing lang known for its dynamic typing, simplicity and versality.

Meaning of basic terms used above:-

High level --> Human readable lang (need to converted into machine understanding)
Low Level language -> which is written on machine code used by hardware RAM, CPU

Interpreted --> code will executed line by line it will be interpreted by python interpreter and converted into byte code which will then run my machine hardware.
Parsing happens its basically slow 
it can run each and every machine 

complied means --> it will be executed all at once , it is faster example c++,c# languages

Versality ---> It can be used by everyone, clean code , easy readiablity  

Dynamic typing --> it already assumes the data type 
ex in c ,c++ = int length_of_land =100
but in python 
length_of_land = 100 its stored automatically

---------------------------------------------------------------------------------
What is Variable ??

anything that can be changed
ex- if i want to build a house we need length , breadth 
length= 100ft
breadth= 100ft

whenever anything we execute it always run on RAM

how to know where the variable is been stored we can use id(variable_name)- checkout variable.python
Incase when both the variable is pointing towards same value it will be stored into same object

Variable naming convention
- can be used a_z,_ both upper and lower case
- number can be used but not in the starting 
- case sensative
- break ,pass , if keywords should not be used in variable
- camelcasing

---------------------------------------------------------------

What is Data Type
1. Integer 
2. Float
3. String
4. Boolean


##### Lecture 2 ####

1. Why do we need print statement
2. How can we print line number for debugging 
3. What is escape squence and how to use it
4. What is String formatting


1. Answer : - for debugging 
print("lenght of the land is ",length_of_land)


4. String formatting 
f string , .format method 

Here we have introduced loguru whenever we use any library in the code we should create requirement.txt 


##### Lecture 3 ####

1. What are the python operators 
2. How BODMAS rule works here 
3. What is the floor and CIEL in python 
4. What is modulo operator 
5. What are the types of type casting 
6. How can i take input from user

what is the operators?
operation --> that we are going to perform on any numbers
like sum , sub ,mul , divide, mod , floor division, power , Absolute

## what are type of typecasting 

1. explicit typecasting -- as a developer we are casting 
2. Implicit typecasting -- when python internally does it 

###### Lesson 4  ##########

IF ELSE and ELIF

1. To check if output is expected or not.
2. Check whether variable or list is not empty -- discussed in if_else_lecture
3. Check if dataframe is not empty -- dataframe is part of pandas or pyspark we will read this later 
4. Backdated job run -- for instance we need to run the job of backdated i.e for previous date in that case we have to use it 
5. To raise some error -- we have to use logger.info and use under if else condition to get the error

conditional operator 
+,-,*,/
1. less than
2. greater than
3. equal to 
4. less than or equal to 
5. greater than or equal to
6. not equals to