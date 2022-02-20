max_len = 0
s="abcabcbb"
arr=[]
k=[1,2,3,4]
for i in range(len(s)):

    if s[i] not in arr:
        arr.append(s[i])
        max_len=max(max_len,len(arr))
    else:
        max_len=max(max_len,len(arr))
        arr = arr[arr.index(s[i])+1:]
        arr.append(s[i])   
print(max_len)

        