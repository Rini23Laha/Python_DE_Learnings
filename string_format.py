Length_of_land = 100
breadth_of_land = 100
cost_of_brick= 20
print("lenght_of_land ",Length_of_land)
print("breadth_of_land ",breadth_of_land)

## suppose we want to print print statement in 2 line  we will use escape sequence we have to use \n
print("my home is of 4 bhk \nLenghth of the home is 100")
print('''my home is of 4 bhk 
      Lenghth of the home is 100''')

### suppose we want "" inside print statement

print("my home is of '4 bhk'")
print('my home is of "4 bhk"')
print("my home is of \t \"4 bhk\"") ### this will give escape character upto 4

### f string , .format method 

print(f"cost of bricks per unit is Rs.{cost_of_brick}/- ")

###### .format method for each varaible currley bracket will be used

print("cost of bricks per unit is Rs {}".format(cost_of_brick))

import logging
from loguru import logger

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

logging.info("cost of bricks per unit is Rs {}".format(cost_of_brick))
logger.info(f"cost of bricks per unit is Rs.{cost_of_brick}/-")