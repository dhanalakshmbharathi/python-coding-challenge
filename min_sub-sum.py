target = 7
nums = [2,3,1,2,4,3]
left = 0
res = len(nums)
curr_sum = 0
    
for i in range(len(nums)): 
    curr_sum += nums[i]
    while curr_sum >= target: 
        res = min(res, i + 1 - left) 
            
        curr_sum -= nums[left] 
        left += 1 
print(res)
    
   
 