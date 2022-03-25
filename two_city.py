def twoCitySchedCost(costs) -> int:
    
    costs.sort(key=lambda x: x[0] - x[1])
    
    tot, i, mid = 0, 0, len(costs) // 2
    while i < mid:
        tot += costs[i][0] + costs[i+mid][1]
        i += 1
    
 
    return tot
costs = [[10,20],[30,200],[400,50],[30,20]]
print(twoCitySchedCost(costs))