#kind of list, used to store them a seq of objects
#tuples are immutable (unchangeble) - can not change them, once we create them
# numbers = [1,2,3] ----> LIST
# numbers = (1,2,3) ---> tuple

numbers = (1,2,3)
print(numbers[0])
#numbers[0] = 10

numbers = (1,2,3,3,3)
numbers.count(3)
print(numbers.count(3))

numbers = (1,2,3,3)
numbers.index(2)
print(numbers.index(2))

#o/p
#1
##numbers[0] = 10 - TypeError: 'tuple' object does not support item assignment
#3
#1
