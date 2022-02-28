m=[[1, 2, 3], 
[4 ,5 ,6],
[7 ,8 ,9 ]]
row=len(m)
col=len(m[0])
for i in range(row):
    for j in range(i,col):
        m[i][j],m[j][i]=m[j][i],m[i][j]
    m[i].reverse
print(m)

        
