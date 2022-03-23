def minSteps( n: int) -> int:

    step, curLen, copyLen = 0, 1, 1
    while curLen < n:
        nextCopyLen = curLen + copyLen 
        curLen += copyLen 
        if (n - nextCopyLen) % nextCopyLen: 
            step += 1 
        else:
            copyLen = nextCopyLen 
            step += 2
    return step 

print(minSteps(4))

