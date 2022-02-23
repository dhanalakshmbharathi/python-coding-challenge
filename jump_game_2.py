nums = [2,3,1,1,4]
# dp=[float('inf') for i in range(len(nums))]
# dp[0]=0
# for i in range((n)):
#     for j in range(1,(nums[i]+1)):
#         if(i+j<n):
#             dp[i+j]=min(dp[i+j],dp[i]+1)
# print(dp[-1])
max_pos=0
curr=0
jump_count=0
for i in range(len(nums)-1):
    max_pos=max(max_pos,nums[i]+i)
    if(curr==i):
        curr=max_pos
        jump_count+=1

print(jump_count)