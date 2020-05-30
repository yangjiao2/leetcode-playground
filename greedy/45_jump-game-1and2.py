# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2


class Solution:
    def jump(self, nums: List[int]) -> int:
        i = curmax = end = step = 0
        for i in range(len(nums) - 1):
            curmax = max(curmax, i + nums[i])
            print(i, end, curmax)
            if i == end:
                print('step', step)
                step += 1
                end = curmax
        return step

    def canJump(self, nums: List[int]) -> bool:
        i = curmax = end = step = 0
        for i in range(len(nums)):
            curmax = max(curmax, i + nums[i])
            print(i, end, curmax)
            if i == end:
                step += 1
                end = curmax
        return end >= len(nums) - 1