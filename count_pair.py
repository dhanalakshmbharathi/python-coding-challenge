arr=[1, 5 ,7 ,1]
sum=6
n=len(arr)
m = dict()

for i in range(n):
    if arr[i] in m.keys():
        m[arr[i]] += 1
    else:
        m[arr[i]] = 1

twice_count = 0
for i in range(0, n):
    if (sum-arr[i]) in m.keys():
        twice_count += m[sum - arr[i]]
    if (sum - arr[i] == arr[i]):
        twice_count -= 1

print(int(twice_count / 2))
