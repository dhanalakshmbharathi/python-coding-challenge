flowerbed = [1,0,0,0,1]
n = 1
count=0
flowerbed = [0] + flowerbed + [0]
print(flowerbed)
for i in range(1,len(flowerbed)-1):
    
    if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
        count+=1
        flowerbed[i] =1
        
print(count>=n)