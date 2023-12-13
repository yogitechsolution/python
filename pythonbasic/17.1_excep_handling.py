#exception handling
age = 20
print(age) #20

age = "age"
print(age) #age

age = age
print(age) #age

age = ("Age: ")
print(age) #Age: 

age = input("Age: ")
print(age) #Age: (??) then enter 30 then it will print 30

#age = int(input(("Age: ")))
#print(age) # Age: (aa) o/p exception ValueError: invalid literal for int() with base 10: 'aa'

try:
    age = int(input(("Age: ")))
    print(age)  #Age: qq
except ValueError:
    print("Invalid value") #Invalid value


