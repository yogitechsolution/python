# Error handling - menas exception handling
# exit code 0 means - prog terminated successfully
# exit code 1 - means prog crashed

#age = int(input("Age: "))
#print(age)

#o/p
#20 - in case you give input as 20
#ValueError - in case you give string other than number e.g asd
# So now handel that value error exception as below:

#try:
    #age = int(input("Age: "))
    #print(age)
#except ValueError:
    #print("Invalid Value")


#o/p
#30 - in case you give input as 30
#Invalid Value - in case you give string other than number e.g asd

#Multiple error handling
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age can not be 0")

#o/p
#40 - in case you give input as 40
#ZeroDivisionError - in case you give a value 0