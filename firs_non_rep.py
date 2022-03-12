def FirstNonRepeating( A):
    m={}
    i=0
    n=len(A)
    res=""
    prev=0
    while(i<n):
        
        if  A[i] in m:
            
            m[A[i]]+=1
        else:
            m[A[i]]=1
        if m[A[prev]]<2:
            res+=A[prev]
        else:
            while prev<i+1:
                if m[A[prev]]<2:
                    break
                prev+=1
            if prev==i+1:
                res+='#'
            else:
                res+=A[prev]
        i+=1
    return res    

print(FirstNonRepeating("aabc"))