# Q1. Define a variable of all the labours and print the name of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
#     labour variable should be something like this 1st_labour, 2nd_labour and so on.
import loguru
from loguru import logger

labour_names = {
    "1st_labour_name": "Mahesh",
    "2nd_labour_name": "Mithilesh",
    "3rd_labour_name": "Ramesh",
    "4th_labour_name": "Sumesh"
}

labour_wages = {    
    
    "1st_labour_wage": 500,
    "2nd_labour_wage": 400,
    "3rd_labour_wage": 400,
    "4th_labour_wage": 300}

logger.info(f"name of all the labours are  {labour_names ['1st_labour_name'], ['2nd_labour_name'], ['3rd_labour_name'], ['4th_labour_name']}" )



# Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
#     labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
#     2nd_labour_wage and so on.
#     You are bound to use string formatting

logger.info(f"The name of the 1st labour is {labour_names['1st_labour_name']} and their daily wage is {labour_wages['1st_labour_wage']}.")
logger.info(f"The name of the 1st labour is {labour_names['2nd_labour_name']} and their daily wage is {labour_wages['2nd_labour_wage']}.")
logger.info(f"The name of the 1st labour is {labour_names['3rd_labour_name']} and their daily wage is {labour_wages['3rd_labour_wage']}.")
logger.info(f"The name of the 1st labour is {labour_names['4th_labour_name']} and their daily wage is {labour_wages['4th_labour_wage']}.")


# Q3. I want to print this paragraph and its line number from which this paragraph is printing
#     """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
#     we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
#     help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
#     we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
#             I have to print this paragraph as it is given here."""

logger.info(f'''"""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here."""''')

# Q4. When do we get NameError?

logger.info(f"we get the name error when we have give the variable name as something else but while printing the variable  \
            we are calling it with different name")

# Q5. Python is a high level language. What does that mean by high level?

logger.info(f"its because the code is written in human understandle language which is then converted by RAM   \
            to make it machine understandtable then the codes will be executed its user friendly   \
            Low Level language -> which is written on machine code used by hardware RAM, CPU")

# Q6. What is compiled and Inetrpreted language, list a few?

# logger.info{f"complied language are those which are been complied before executing the code such as C in C, C++ we have define the datatype   \
#             of the variable before assigning the values where as in python which is the interpreted language the datatype were given  \
#             automatically that is datatype are already predefined if we write var1 = 10 python will undertsnad var1 is a integer "}

# Q7. Get all varibales address from RAM and you find if something is similar?

logger.info(f"The address of the 1st labour is {id(labour_names['1st_labour_name'])} and their daily wage address is {id(labour_wages['1st_labour_wage'])}.")
logger.info(f"The address of the 1st labour is {id(labour_names['2nd_labour_name'])} and their daily wage address is {id(labour_wages['2nd_labour_wage'])}.")
logger.info(f"The address of the 1st labour is {id(labour_names['3rd_labour_name'])} and their daily wage address is {id(labour_wages['3rd_labour_wage'])}.")
logger.info(f"The address of the 1st labour is {id(labour_names['4th_labour_name'])} and their daily wage address is {id(labour_wages['4th_labour_wage'])}.")