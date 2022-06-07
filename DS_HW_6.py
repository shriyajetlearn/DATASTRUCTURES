def merge_sort_descending(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort_descending(left)
        merge_sort_descending(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


nums = [7, 3, 2, 8, 1, 4, 5, 9, 6, 10]
merge_sort_descending(nums)
print(f'nums list sorted with merge sort: {nums}')
