from loguru import logger 
labour_with_cost ={"Mahesh":400,"Ramesh":500,"govind":900}
# logger.info(labour_with_cost)
# logger.info(labour_with_cost.keys())
# logger.info(labour_with_cost.values())
# logger.info(labour_with_cost.items())

for key in labour_with_cost:
    logger.info(f"{key,labour_with_cost[key]}")

for key,value in labour_with_cost.items():
    logger.info(f"{key,value}")

#### Commonly used dictionary method)
print(labour_with_cost.get("Mahesh"))
