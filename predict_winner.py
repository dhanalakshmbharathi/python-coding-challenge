def ok(nums, l: int, r: int,chance :int):
    if(l>r):
        return False
    elif(chance==0):
        
        return max(nums[l]+ok(nums,l+1,r,1),nums[r]+ok(nums,l,r-1,1))
        
    else:
        return min(ok(nums,l,r-1,0),ok(nums,l+1,r,0))
nums = [1,5,2]           
sum_of_nums=sum(nums)
i=0
j=len(nums)-1
one=ok(nums,0,j,0)
two=sum_of_nums-one
print(one>=two)
    
