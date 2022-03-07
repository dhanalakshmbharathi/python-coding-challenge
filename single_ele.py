# def single_element(arr):
#     n=len(arr)
#     index=n-1
#     while(index>=0):
#         if arr[index] !=arr[index-1]:
#             return arr[index]
#         index+=2
#     return None
def single_element(arr):
    n = len(nums) - 1
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or nums[mid-1] != nums[mid]) and (mid == n or nums[mid+1] != nums[mid]):
            return nums[mid]
        elif nums[mid+1] == nums[mid]:
            if mid % 2 == 1:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if mid % 2 == 1:
                left = mid + 1
            else:
                right = mid - 1
    

nums = [1,1,2,3,3,4,4,8,8]
print(single_element(nums))