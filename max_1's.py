# def rowWithMax1s(self,arr, n, m):
#     res=[]
#     for i in range(len(arr)):
#         s=arr[i].count(1)
#         res.append(s)
#     max_index=res.index(max(res))
#     if max(res)==0:
#         return -1
#     else:
#         return max_index

def rowWithMax1s(arr, n, m):
    max_index=-1
    c=m-1
    r=0
    while r<n and c>=0:
        
        if arr[r][c]==1:
            max_index=r
            c-=1
        else:
            r+=1
    return max_index    

N = 4 
M = 4
Arr= [[0, 1, 1, 1],
       [0, 0, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]        
print(rowWithMax1s(Arr,N,M))