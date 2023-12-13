#Program to check name length

name = input("Enter name: ")
if len(name) < 3:
    print("Name must be min 3 characters long")
elif len(name) > 10: #(3, 10)
    print ("Name can not be more than 10 characters long")
else:
    print("Name looks good!")
print("Name length: " + str(len(name)))

#o/p
#Enter name: Yogi Sriva
#Name looks good!
#Name length: 10

#Enter name: Yo
#Name must be min 3 characters long
#Name length: 2

#Enter name: Yogendra Srivastava
#Name can not be more than 10 characters long
#Name length: 19