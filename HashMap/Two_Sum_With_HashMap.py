# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return([hashmap[complement], i])

            hashmap[num] = i


solution = Solution()
print(solution.twoSum(nums, target))