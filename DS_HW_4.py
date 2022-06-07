def lower_bound(num, nums):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if num <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left # can return right as well

def upper_bound(num, nums):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if num < nums[mid]: # only difference between lower_bound() and upper_bound()
            right = mid
        else:
            left = mid + 1
    return left # can return right as well

num = 2
nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8]

lower_bound_result = lower_bound(2, nums)
upper_bound_result = upper_bound(2, nums)

print(f'Lower bound result = {lower_bound_result}')
print(f'Upper bound result = {upper_bound_result}')
