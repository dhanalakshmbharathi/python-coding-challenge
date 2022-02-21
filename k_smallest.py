import math
import heapq
from multiprocessing.sharedctypes import Value
from optparse import Values
points = [[1,3],[-2,2]]
k = 1
# result = []
# for i, point in enumerate(points):
#     distance = pow(pow(point[1] , 2) + pow(point[0], 2), 0.5)
#     result.append([distance, point])
# print( [x[1] for x in sorted(result)][0:k])


#heapq
def distance(x, y):
        return math.sqrt(x**2 + y**2)       
hashMap = {}        
for i in range(len(points)):
    x,y = points[i][0], points[i][1]
    temp = distance(x,y)
    hashMap[i] = temp            				
result = heapq.nsmallest(k, hashMap.keys(), key = hashMap.get)
output = []
for i in result:
    output.append(points[i])
print(output)
        