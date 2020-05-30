# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input:nums = [1,1,1], k = 2
# Output: 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc, result = 0, dict()
        counter = 0
        for i in range(len(nums)):
            num = nums[i]
            acc += num
            temp = (len(result[acc - k]) if acc - k in result else 0)
            temp1 = (1 if acc == k else 0)

            if acc not in result:
                result[acc] = [i]
            else:
                result[acc].append(i)
            print(temp, temp1)
            counter += temp + temp1
        return counter