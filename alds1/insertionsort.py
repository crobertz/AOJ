N = int(input())
nums = [int(n) for n in input().split()]

def insertionSort(nums):
    for i in range(len(nums)):
        a = nums[i]
        j = i-1

        while j >= 0 and nums[j] > a:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = a

        print(' '.join([str(n) for n in nums]))

insertionSort(nums)