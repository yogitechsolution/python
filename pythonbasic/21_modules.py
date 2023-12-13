# Modules: A file with some python code.
# We use modules to org our code into file.
# e.g. different section in super market for fruits, grossary etc..

#def lbs_to_kg(weight): #From line 5 to 10 (2 fun) we have moved to another file as per module concept
    #return weight * 0.45


#def kg_to_lbs(weight):
    #return weight / 0.45

#kg = lbs_to_kg(170)
#print(kg) # 76.5
#lbs = kg_to_lbs(76)
#print(lbs) #168.88888888888889

import modules_call #Calling module 1 way
print(modules_call.kg_to_lbs(76)) # 168.88888888888889

import modules_call
from modules_call import lbs_to_kg #Calling module ANOTHER way
print(lbs_to_kg(170)) # 76.5