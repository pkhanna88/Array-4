# Time Complexity: O(sort)
# Space Complexity: O(sort)
# Did this problem run on Leetcode: Yes
# Any issues faced doing this problem: No

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum([nums[i] for i in range(0, len(nums), 2)])