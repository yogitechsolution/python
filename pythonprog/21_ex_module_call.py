#Calling modules (utils.py) from another files (modules)

import utils #Calling module 1 way
numbers = [3,6,2,8,4,10]
print(utils.find_max(numbers)) #10

print(max(numbers)) #10 # It is because max itself a built in fun of python

import utils
from utils import find_max #Calling module ANOTHER way
numbers = [50,30,60,10]
print(find_max(numbers)) #60

print(max(numbers)) #60 # It is because max itself a built in fun of python