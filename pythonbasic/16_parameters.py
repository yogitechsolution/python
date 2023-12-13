#Parameters: are placeholder for receiving informtion e.g. to pass parameter in functions
#Arguments - actual piece of info which we supply to parameters
#positional arguments - means order matters
#keyword arguments - e.g. last_name="K" - for improve readability, specially numbers parameters

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print('Start') #execution of prog starts here!
greet_user("Yogi" , "Srivastava")  #calling function 
greet_user(last_name="K", first_name="Divya")  #calling function 
print('Finish')

#o/p
#Start
#Hi Yogi Srivastava!
#Welcome aboard
#Hi Divya K!
#Welcome aboard
#Finish