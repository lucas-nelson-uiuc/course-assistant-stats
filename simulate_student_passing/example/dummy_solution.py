def dummy_solution(nums):
    x, y, z = nums
    if (x % 2 == 0) & (y % 2 == 0) & (z % 2 == 0):
        return -1
    elif (x % 2 != 0):
        return x
    elif (y % 2 != 0):
        return y
    elif (z % 2 != 0):
        return z
    else:
        return x