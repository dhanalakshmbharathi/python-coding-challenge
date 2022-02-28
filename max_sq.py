matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

num_rows = len(matrix)
num_cols = len(matrix[0])
dp = [[0 for i in range(num_cols+1)] for j in range(num_rows+1)]
area = 0
for i in range(1, num_rows+1):
    for j in range(1, num_cols+1):
        if matrix[i-1][j-1] == '1':
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
            area = max(area, dp[i][j]*dp[i][j])
print(area)