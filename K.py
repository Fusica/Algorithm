# Editor: Max

# Create Time: 9/1/21 17:36


def partition(nums, low, high):
    pivot = nums[low]
    while low < high:
        while low < high and pivot <= nums[high]:
            high -= 1
        nums[low] = nums[high]
        while low < high and pivot >= nums[low]:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low


def find(nums, n, k):
    low = 0
    high = n - 1
    while True:
        tmp = partition(nums, low, high)
        if tmp == k - 1:
            return nums[tmp]
        elif tmp < k - 1:
            low = tmp + 1
        else:
            high = tmp - 1


n, k = input().split()
n = int(n)
k = int(k)
a = input()
num = [int(n) for n in a.split()]
print(find(num, n, k))
