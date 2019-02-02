def _partition(nums, front, end):
    i = front
    pivot = nums[end]
    for j in range(front, end):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
    else:
        nums[i], nums[end] = nums[end], nums[i]

    return i

def quick_sort(nums, front, end):

    if front < end:
        pivot = _partition(nums, front, end)

        quick_sort(nums, front, pivot-1)
        quick_sort(nums, pivot+1, end)


nums = [5, 3, 8, 6, 2, 7, 1, 4]
print(nums)
quick_sort(nums, 0, len(nums)-1)

print(nums)