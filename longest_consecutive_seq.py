nums = [100,4,200,1,2,3]
# nums=sorted(list(set(nums)))
# curr=1
# k=1
# for i in range(len(nums)):
#     if(nums[i-1]+1==nums[i]):
#         curr+=1
#     else:
#         curr=1
#     k=max(k,curr)
# print(k)

s=set(nums)
longest=0
for num in nums:
    if(num-1) not in s:
        length=0
        while(num+length in s):  
            length+=1
        longest=max(longest,length)
print(longest)





