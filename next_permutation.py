arr = [3,2,1]
n=len(arr)
if(n<=2):
    arr.reverse()
pointer=n-2
while(pointer>=0 and arr[pointer]>=arr[pointer+1]):#finding the index of first element that breaks the decending nature of array
    pointer-=1   
if pointer==-1:  #no break away from descending
    (arr.reverse)
    print(arr)
for i in range(n-1,pointer,-1):
    if(arr[i]>arr[pointer]):# swap the break away element with the next greater number
        arr[i],arr[pointer]=arr[pointer],arr[i]
        break
arr[pointer+1:]=reversed(arr[pointer+1:])#reverse all ele between the swapped elements

print(arr)




