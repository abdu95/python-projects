# matrix - rectangular array of numbers (rows and columns)
# 3x3 matrix
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# we can model this in python using a 2 dimensional list - a list where each item in that list is another list
# each item in this list, is going to be another (one separate) list, and that list represents the items in each row
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])

#  in each iteration row will contain 1 list
for row in matrix:
    for number in row:
        print(number)

