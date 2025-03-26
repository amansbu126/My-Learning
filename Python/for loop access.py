from loguru import logger
labour_name=["mahesh","ramesh","dipesh","goesh"]

for i in range(len(labour_name)):
    logger.info(f"Labour {i+1} is {labour_name[i]}" )