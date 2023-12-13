# Use it to iterate over items of a collection e.g. string/list/range - anything has multiple items
# string is a collection of characters

for item in 'Python': #via list string
    print(item)

for item in ['Yogi', 'Divya', 'Leo']: #via list names
    print(item)

for item in [1, 2, 3]: #via list numbers
    print(item)

for item in range(5): #via biltin fun range - 5 is not included
    print(item)

for item in range(7, 10): #via biltin fun range - between 7 to 10 (10 excluded)
    print(item)

for item in range(10, 18, 2): #via biltin fun range - gap of 2 starting from 10 (last number excluded)
    print(item)


#o/p
#P
#y
#t
#h
#o
#n
#Yogi
#Divya
#Leo
#1
#2
#3

#0
#1
#2
#3
#4

#7
#8
#9

#10
#12
#14
#16