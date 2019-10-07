def matrix_spiral_print(M):
list = []
for y in len(M[0]):
    for x in len(M):
        list.append(M[x,y])
return list
# Fill this in.

grid = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12