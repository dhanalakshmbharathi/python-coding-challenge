grid = [[1,3,1],[1,5,1],[4,2,1]]
dp=[[0]*len(grid[0])]*len(grid)
print(dp)
row=len(grid)
col=len(grid[0])
for i in range(row):
    for j in range(col):
        if (i==0 and j==0):
            dp[i][j]=grid[i][j]
        elif(i==0):
            dp[i][j]=grid[i][j]+dp[i][j-1]
        elif(j==0):
            dp[i][j]=grid[i][j]+dp[i-1][j]
        else:
            dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])