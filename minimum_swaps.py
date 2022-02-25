


arr =[20, 3 ,5, 4 ,14 ,7 ,11, 1, 9, 10, 3 ,9] 
k = 19
# c=0
# mi=9876553
# if(len(arr)<=2):
#     print(0)
# c = len([i for i in arr if i <= k])

# for i in range(len(arr)-(c)+1):
#     w=0
#     for j in range(i,i+c):
#         if(arr[j]>k):
#             w+=1
#         else:
#             continue
#     mi=min(w,mi)
# print(mi)

x = len([i for i in arr if i <= k])

c=len([i for i in arr[:x] if i > k])
res=c

i=0
j=x
while(j<len(arr)):
    if(arr[i]>k):
        c-=1
    if(arr[j]>k):
        c+=1
    res=min(c,res)
    i+=1
    j+=1
print(res)

