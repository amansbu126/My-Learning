""" 
*
* *
* * *
* * * *
* * * * *
"""
from loguru import logger
i_input = int(input("please provide your input "))


for i in range(i_input+1):
  for j in range(i):
    print('*',end=' ')
  print('\n')