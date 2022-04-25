def maxChunksToSorted( arr) -> int:
    n = len(arr)
    i = 0
    ans = 0
    sum_ = 0
    i_sum = 0
    while i<n:
        sum_ += arr[i]
        i_sum += i
        if sum_==i_sum:
            ans += 1
            sum_ = 0
            i_sum = 0
        i += 1
    return ans

print(maxChunksToSorted(arr = [4,3,2,1,0]))