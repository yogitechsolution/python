# Print F shape via * by using nested loop

numbers = [5, 2, 5, 2, 2]
for item in numbers:
    #print('x' * item)
    output = ''
    for count in range(item):
        output += 'x'
    print(output)

#o/p
#xxxxx
#xx
#xxxxx
#xx
#xx
