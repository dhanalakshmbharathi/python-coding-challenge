nums = [1,3,6]
# nums=sorted(nums)
# max_arr=[]
# min_arr=[]
# for i in nums:
#     max_arr.append(i+k)
#     min_arr.append(i-k)
# min_val = min(i for i in max_arr if i > 0)
# max_val=max(i for i in min_arr if i>0)
k = 3
nums.sort()
res=nums[-1]-nums[0]
for i in range(len(nums)-1):
    min_val=min(nums[0]+k,nums[i+1]-k)
    max_val=max(nums[-1]-k,nums[i]+k)
    res=min(res,max_val-min_val)
print(res)