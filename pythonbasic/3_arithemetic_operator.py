#Order of operation: 
#parenthesis ()
#exponentiation 2**3
#multiplication or division
#addition or subtraction

print (10 + 3)
print (10 - 3)
print (10 * 3)
print (10 / 3)
print (10 // 3)
print (10 % 3)
print (10 ** 3)

x = 10
print (x)

x = 10
x = x + 3
print ("Arthemetic operatore: " + str(x))

y = 10
y += 3
print ("Argumented assignment operatore: " + str(y))

z = 10 + 3 * 2
print (z)

z = (10 + 3) * 2
print (z)

x = 3 > 2
print (x)

x = 3 == 2
print (x)

x = 3 != 2
print (x)

x = 10 + 3 * 2 ** 2
print(x)

x = (10 + 3) * 2 ** 2
print(x)

#Output

#13
#7
#30
#3.3333333333333335
#3
#1
#1000
#10
#Arthemetic operatore: 13
#Argumented assignment operatore: 13
#16
#26
#True
#False
#True
#22
#52