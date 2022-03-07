# Search a 2D Matrix II

# Write an efficient algorithm that searches for a value target in
#  an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
def searchMatrix( matrix, target):
    M = len(matrix)
    N = len(matrix[0])
    r = M - 1
    c = 0    
    while c < N and r > -1:
        if matrix[r][c] > target:
            r -= 1
        elif matrix[r][c] < target:
            c += 1
        else:
            return True

    return False
    
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
