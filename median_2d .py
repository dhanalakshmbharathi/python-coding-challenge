
def no_of_ele(row,mid,r):
    l=0
    h=r-1
    while(l<h):
        md=(l+h)//2
        if row[md]<=mid:
            l=md+1
        else:
            h=md-1
    return l
def median( matrix):
    low=1
    high=1e9
    n=len(matrix)
    m=len(matrix[0])
    while(low<=high):
        mid=(low+high)//2
        count=0
        for i in range(n):
            row=matrix[i]
            count+=no_of_ele(row,mid,n)
        if count<=int((n*m)/2):
            low=mid+1
        else:
            high=mid-1
    return low

M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]
r=3
c=3
print(median(M))

