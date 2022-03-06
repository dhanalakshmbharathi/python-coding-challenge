def spirally(m,r,c):
    left=0
    right=c-1
    top=0
    down=r-1
    dirr=0
    ans=[]
    while(top<=down and left<=right):
        if dirr==0:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            dirr=1
        elif dirr==1:
            for i in range(top,down+1):
                ans.append(matrix[i][right])
            right-=1
            dirr=2
        elif(dirr==2):
            for i in range(right,left-1,-1):
                ans.append(matrix[down][i])
            down-=1
            dirr=3
        elif(dirr==3):
            for i in range(down,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
            dirr=0
    return ans
r = 4
c = 4
matrix = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15,16]]
print(spirally(matrix,r,c))