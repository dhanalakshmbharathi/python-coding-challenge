
arr = [-2,1,-3,4,-1,2,1,-5,4]
# brute force
# sum=0
# max_sum1=-23456789123456789
# max_sum=-98765412

# for i in range(len(arr)):
#     max_sum1=arr[i]
#     sum=arr[i]
#     for j in range(i+1,len(arr)):
#         sum+=arr[j]
#         max_sum1=max(max_sum1,sum)
#     max_sum=max(max_sum,max_sum1)

# print(max_sum)

#o(n)
curr_sum=arr[0]
max_sum=arr[0]
for i in arr[1:]:
    curr_sum+=i
    if(curr_sum<i):
        curr_sum=i
    if(max_sum<curr_sum):
        max_sum=curr_sum
print(max_sum)
