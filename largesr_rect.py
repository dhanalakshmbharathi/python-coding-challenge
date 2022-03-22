def largestRectangleArea( heights) :

    length = len(heights)
    growth = []        
    maxArea, idx = heights[0], 0
    while idx < length:
        curr = heights[idx]
        if not growth or curr > growth[-1][0]:
            growth.append((curr, idx))        
        if curr < growth[-1][0]:              
            while growth and curr < growth[-1][0]:
                last = growth.pop()
                maxArea = max(maxArea, last[0] * (idx - last[1]))      
            growth.append((curr, last[1]))   
        idx += 1
    while growth:        
        last = growth.pop()
        maxArea = max(maxArea, last[0] * (idx - last[1]))
    return maxArea

print(largestRectangleArea(heights = [2,4]))

