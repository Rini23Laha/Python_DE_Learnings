### whenever there will be conditional operator the value will be either true or false 
import loguru
from loguru import logger

a = 5
lengh_of_land = 100
bricks_of_land = 200
labour_mis = "jagmohan"
is_home = True 
lenght_of_land = 200
print(a>5)
print(a>=5)


#### Always use logger.info to check the line numbers properly 
## 2. Each and every line will be executed only if the condition is true otherwise condition wont run


lenght_of_land = int(input("Enter the length : "))

if lenght_of_land < 100:
    logger.info (f"your length given for the land is incorrect")
elif lengh_of_land > 500:
    logger.info(f"you can build 2 house")
else:
    logger.info(f"Share us more details about the bredth")


## How will you find out if given number by user is even or odd
## we need to use modulo operator


Number = int(input("Enter the number to check: "))
if Number%2 == 0:
    logger.info("Number is even")
else:
    logger.info("Number is odd")