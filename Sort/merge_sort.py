import sys


def merge(nums, start, mid, end):
    left_nums = nums[start: mid]
    right_nums = nums[mid: end]

    left_nums.append(sys.maxsize)
    right_nums.append(sys.maxsize)

    merge_nums = []
    l_idx = 0
    r_idx = 0

    for idx in range(start, end):
        if left_nums[l_idx] < right_nums[r_idx]:
            nums[idx] = left_nums[l_idx]
            l_idx += 1
        else:
            nums[idx] = right_nums[r_idx]
            r_idx += 1


def merge_sort(nums, start, end):

    if start < end-1:
        mid = int((start + end)/2)

        merge_sort(nums, start, mid)
        merge_sort(nums, mid, end)

        merge(nums, start, mid, end)



def main():
    nums = [5, 3, 8, 6, 2, 7, 1, 4]
    print(nums)

    merge_sort(nums, 0, len(nums))
    print(nums)


if __name__ == "__main__":
    main()
