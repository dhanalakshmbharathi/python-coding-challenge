def searchMatrix( matrix, target):
        n=len(matrix)
        m=len(matrix[0])-1
        row=0
        while(row<n):
            if(matrix[row][-1]<target):
                row+=1
            else:
                for i in range(m,-1,-1):
                    if(matrix[row][i]==target):
                        return True
                    else:
                        continue
                return False

M=[[1],[3]]
t=3
print(searchMatrix(M,t))