def sort_numbers(arr):
    if len(arr) <= 1:
        return arr

    divider = arr[len(arr) // 2]
    left = [number for number in arr if number < divider]
    middle = [number for number in arr if number == divider]
    right = [number for number in arr if number > divider]

    return sort_numbers(left) + middle + sort_numbers(right)


def verify_array_format(nums):
    if nums is None or not isinstance(nums, list) or len(nums) <= 1:
        return False

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False

    return True


def find_duplicate(nums):
    num_set = set()

    is_array_correct = verify_array_format(nums)
    if not is_array_correct:
        return False

    for num in nums:
        if num in num_set:
            return num
        else:
            num_set.add(num)

    return False
