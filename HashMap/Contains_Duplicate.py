# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.




class Solution:
    def containsDuplicate(self,nums):
        hashmap = {}

        for num in nums:

            if num in hashmap:
                return True
            hashmap[num] = True
        return False
    
nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))
