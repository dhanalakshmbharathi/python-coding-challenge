def maxIncreaseKeepingSkyline( grid) -> int:
    total_sum = 0
    row_max = []
    col_max = [max(row) for row in grid]
    for i in range(len(grid[0])):
        temp_max = 0
        for j in range(len(grid)):
            if temp_max < grid[j][i]:
                temp_max = grid[j][i]
        row_max.append(temp_max)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total_sum += min(row_max[j], col_max[i]) - grid[i][j]               
    return total_sum


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))