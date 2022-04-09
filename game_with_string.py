from collections import Counter
import heapq

def minValue( s, k):
    
    d = Counter(s)
    c = list(d.values())
    c = [i*-1 for i in c]
    heapq.heapify(c)
    while k>0:
        temp = heapq.heappop(c)
        temp +=1
        heapq.heappush(c, temp)
        k-=1
    sum1 = 0
    for i in c:
        sum1+=i**2
    return sum1


s = "abccc"
k = 1
print(minValue(s,k))