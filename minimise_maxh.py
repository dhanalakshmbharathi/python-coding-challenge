k = 5
n = 10
arr= [2 ,6, 3, 4 ,7, 2 ,10, 3 ,2 ,1]
arr.sort()
ans = arr[-1] - arr[0]
small = arr[0] + k
large = arr[-1] - k
for i in range(n-1):
    mn = min(small, arr[i+1] - k)
    mx = max(large, arr[i] + k)
    if mn < 0: continue
    ans = min(ans, mx - mn)
print(ans)