


array=[87, 78 ,16 ,94]
a=36
b=72

k=0
lo=0
j=len(array)-1
while(k<j):
    if(array[k]<a):
        temp=array[k]
        array[k]=array[lo]
        array[lo]=temp
        k+=1
        lo+=1
    elif(array[k]>b):
        temp=array[k]
        array[k]=array[j]
        array[j]=temp
        j-=1
    else:
        k+=1
print(array)