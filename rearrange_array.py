
arr = [12, 11, -13 ,-5, 6 ,-7, 5, -3 ,-6]
# # brute force
# def rotate(arr1,i,j):
#     temp=arr1[j]
#     for k in range(j,i,-1):
#         arr[k]=arr[k-1]
#     arr[i]=temp
#     return arr
# out_of_place=-1
# n=len(arr)
# for index in range(n):
#     if(out_of_place>=0):
#         if((arr[out_of_place]>=0 and arr[index]<0 ) or (arr[out_of_place]<0 and arr[index]>=0)):
#             arr=rotate(arr,out_of_place,index)
#             if(index-out_of_place>2):
#                 out_of_place+=2
#             else:
#                 out_of_place=-1
#     if(out_of_place==-1):
#         if((arr[index]>=0 and index%2==0)or(arr[index]<0 and index%2==1)):
#             temp=index
#             out_of_place=index            
# print(arr)
#using quick sort(changes relative pos.)
k=-1
for i in range(len(arr)):

    if(arr[i]<0):
        k+=1
        arr[i],arr[k]=arr[k],arr[i]
print(arr)

p=k+1
n=0
while(p<len(arr) and n<p and arr[n]<0 ):
    arr[p],arr[n]=arr[n],arr[p]
    p+=1
    n+=2
print(arr)







