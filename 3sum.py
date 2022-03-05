def threeSum( nums):
    ans=[]
    nums.sort()
    for i,ele in enumerate(nums):
        if i>0 and ele ==nums[i-1]:
            continue
        else:
            l=i+1
            r=len(nums)-1
            while(l<r):
                threesum=ele+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    ans.append([ele,nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
    
    return ans
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))