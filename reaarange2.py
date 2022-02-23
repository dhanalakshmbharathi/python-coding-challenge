k=-1
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
for i in range(len(arr)):
    if(arr[i]<0):
        k+=1
        arr[i],arr[k]=arr[k],arr[i]
print(arr)
