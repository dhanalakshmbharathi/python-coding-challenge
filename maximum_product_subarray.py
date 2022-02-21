nums=[2,3,-2,4]
# brute force
# max_pro2=-9876431
# for i in range(len(nums)):
#     max_product1=nums[i]
#     sub_product=nums[i]
#     for j in range(i+1,len(nums)):
#         sub_product*=nums[j]
#         max_product1=max(max_product1,sub_product)
#     max_pro2=max(max_pro2,max_product1)
# print(max_pro2)
# dp
curr_min=1
curr_max=1
res=max(nums)
for n in nums:
    if(n==0):
        curr_min=1
        curr_max=1
        continue
    curr_max1=curr_max
    curr_max=max(curr_min*n,curr_max*n,n)
    curr_min=min(curr_max1*n,curr_min*n,n)
    res=max(res,curr_max)
print(res)

        