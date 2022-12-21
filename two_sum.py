def two_sum(nums, target: int):
    """
    Returns indices of 2 numbers from nums with target sum
    """
    a = nums[::]
    a.sort()
    l = 0
    r = len(nums) - 1
    while l < r:
        if (a[l] + a[r]) == target:
            if a[l] == a[r]:
                return [nums.index(a[l]), nums.index(a[r], nums.index(a[l]) + 1)]
            return [nums.index(a[l]), nums.index(a[r])]
        elif (a[l] + a[r]) > target:
            r -= 1
        else:
            l += 1
    return []

