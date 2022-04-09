from collections import deque
def printFirstNegativeInteger( arr, n, k):
    
    q = deque()
    for i in range(k):
        if arr[i]<0:
            q.append(i)
          
    ans =[] 
    for i in range(k,n):
        if not q:
            ans.append(0)
        else:
            ans.append(arr[q[0]])
        if q and q[0]<=i-k:
            q.popleft()
       
        if arr[i]<0:
            q.append(i)
    if not q:
        ans.append(0)
    else:
        ans.append(arr[q[0]])
    return ans

A= [-8, 2, 3, -6, 10]
K = 2
N=5
print(printFirstNegativeInteger(A,N,K))