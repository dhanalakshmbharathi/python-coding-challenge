def canSeePersonsCount(heights):
    stack=[]
    ans=[]
    ans.append(0)
    stack.append(heights[-1])
    for i in range(len(heights)-2,-1,-1):
        count=0
        while(stack and stack[-1]<heights[i]):
            stack.pop()
            count+=1
        if(stack):    
            ans.append(count+1)
        else:
            ans.append(count)
        stack.append(heights[i])
    return  ans[::-1]
heights = [10,6,8,5,11,9]
print(canSeePersonsCount(heights))