from loguru import logger

test_tuple =(1,2,3,65,32,True,'Aman')
print(test_tuple)
print(type(test_tuple))

#test_tuple[2]=5

#print(test_tuple)
#TypeError: 'tuple' object does not support item assignment

logger.info(test_tuple[3:5])