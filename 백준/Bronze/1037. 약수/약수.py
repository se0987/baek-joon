N = int(input())
nums = list(map(int, input().split()))


def divisor(N, nums):
    if N == 1:
        return nums[0] ** 2
    lst = sorted(nums)
    if lst[0] == 0:
        return lst[1] * lst[-1]
    else:
        return lst[0] * lst[-1]


print(divisor(N, nums))