# Program to calculate total cost of all the items in a shopping cart

prices = [10, 20, 30]

total = 0
for price in (prices): #via list numbers
    print(price)
    total += price # argumented assignment operator same as total = total + price
print(f"Total: {total}") #Formatted string - a string prefix with f, to dynemically include some value in our string!



#o/p
#10
#20
#30

#Total: 60
