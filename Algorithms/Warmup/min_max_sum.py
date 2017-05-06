def minMax(l):
    nums = sorted(l)
    maximum = sum(nums[1:])
    minimum = sum(nums[:4])
    return minimum, maximum

nums = list(map(int, input().split()))
result = minMax(nums)
print(result[0], result[1])
    