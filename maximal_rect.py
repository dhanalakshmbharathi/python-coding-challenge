
import collections
   
def maximalRectangle( matrix):
        if len(matrix) == 0:
            return 0
        m, n, = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j] = 1 if matrix[i][j] == '1' else 0  
                if matrix[i][j] == 1 and j - 1 >= 0 and matrix[i][j - 1] > 0:
                    matrix[i][j] = matrix[i][j - 1] + 1  
        max_area, mono_stack = 0, collections.deque()
        for j in range(n):  
            mono_stack.clear()
            for i in range(m):
                ii = i
                while len(mono_stack) > 0 and matrix[i][j] < mono_stack[-1][0]:
                    val, ii = mono_stack.pop()
                    max_area = max(max_area, val * (i - ii))
                mono_stack.append((matrix[i][j], ii))
            while len(mono_stack) > 0:
                val, ii = mono_stack.pop()
                max_area = max(max_area, val * (m - ii))
        return max_area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] 
print(maximalRectangle(matrix))