nums = [-2,1,-3,4,-1,2,1,-5,4]
m=-6790986553
current_sum=0
for num in nums:
    current_sum+=num
    m=max(m,current_sum)
    if(current_sum<0):
        current_sum=0
print(m)










