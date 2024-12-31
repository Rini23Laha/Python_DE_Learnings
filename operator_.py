### How to write operator ??
import loguru
from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mis1 = "jaggi"
labour_mis2 = "rann"
is_home = True 

total_area_of_land = length_of_land * breadth_of_land
perimeter_of_land = 2 * (length_of_land + breadth_of_land)

#### Follow here BODMAS rule  

logger.info(f"total area of land = {total_area_of_land}")  
logger.info(f"perimeter of land  = {perimeter_of_land}")  


#### MODULO operator #####

## incase we just want have reminder of the division - Armstrong number code 

### Floor division --> Incase of the floor division it will discard all the numbers after point

### CIEL when we want to use CIEL we need to import math library ciel will give max value ex if 

print(math.ceil(11/4))
print(math.floor(11/4))

## sum of two string will give string this is called concatination 

a= "1"
b ="2"
print(a+b)
print(int(a)+int(b))

## Now suppose we want to add these to string values as integer we need to cast it
## So type casting means converting one data type to another

### How to get user input

length_of_land = int(input("Please enter the lenght of the land"))
breadth_of_land = int(input("please enter breadth of the land"))
total_area_of_land = length_of_land * breadth_of_land
logger.info(f"total area of the land is {total_area_of_land}")