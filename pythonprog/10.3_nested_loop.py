# Adding one loop to another loop
#e.g. can generate list of coordinates (combination of x and y)

for x in range(4): #Outer loop
    for y in range(3): #Inner loop
        print(f'({x}, {y})')

#o/p
#(0, 0)
#(0, 1)
#(0, 2)
#(1, 0)
#(1, 1)
#(1, 2)
#(2, 0)
#(2, 1)
#(2, 2)
#(3, 0)
#(3, 1)
#(3, 2)