"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
from loguru import logger

i_input = int(input("Please provide your input"))

for i in range(1, i_input + 1):
    print(" " * (i_input - i) + "*" * i)