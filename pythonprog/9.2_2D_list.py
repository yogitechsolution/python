#Metrics - rectengular array of numbers
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])

#o/p
#2
#20

for row in matrix:
    for item in row:
        print(item)

#o/p
#1
#20
#3
#4
#5
#6
#7
#8
#9
