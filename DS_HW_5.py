def insertion_sort_descending(nums):
    for i in range(1, len(nums)):
        current_num = nums[i]
        j = i-1
        while j >= 0 and current_num > nums[j] :
                nums[j+1] = nums[j]
                j -= 1
        nums[j+1] = current_num

def bubble_sort_descending(nums):
    n = len(nums)
 
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
  
nums1 = [7, 3, 2, 8, 1, 4, 5, 9, 6, 10]
nums2 = [4, 5, 9, 6, 1, 7, 8, 3, 2, 10]

insertion_sort_descending(nums1)
bubble_sort_descending(nums2)

print(f'nums1 list sorted with insertion sort: {nums1}')
print(f'nums2 list sorted with bubble sort: {nums2}')