def trappingWater(height,n):
    maxLeft = height[0]
    maxRight = height[n-1]
    trappedWater = 0
    left = 1   
    right = n-2
    while(left<=right):
        if(maxLeft<maxRight):
            if(height[left]>=maxLeft):
                maxLeft = height[left]
            else:
                trappedWater += maxLeft-height[left]
            left+=1
        else:
            if(height[right]>maxRight):
                maxRight = height[right]
            else:
                
                trappedWater += maxRight-height[right]
            right-=1
    return trappedWater

height=[0,1,0,2,1,0,1,3,2,1,2,1] 
n=len(height)
print(trappingWater(height,n))