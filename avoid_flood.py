def avoidFlood( rains ):
    d=set()
    full=set()
    l=[]
    ans=[1]*len(rains)
    for i in range(len(rains)):
        if rains[i]!=0 and rains[i] in d:
            l.append(i)
        else:
            d.add(rains[i])
    
    for i in range(len(rains)): 
        if rains[i]:
            if rains[i] in full:
                return []
            full.add(rains[i])
            ans[i] = -1 
        else:
            
            for j in range(len(l)):
                if rains[l[j]] in full:
                    index = l.pop(j)
                    ans[i] = rains[index]
                    full.remove(rains[index])
                    break        
    return ans


rains = [1,2,0,1,2]
print(avoidFlood(rains))
