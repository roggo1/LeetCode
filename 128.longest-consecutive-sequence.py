#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 0
        nums_set = set(nums)
        if len(nums) == 0:
            return 0
        curr = nums[0]
        length = 1
        for i in nums_set:
            if i - 1 not in nums_set:
                length = 1
                curr = i
            
            while curr + 1 in nums_set:
                curr += 1
                length += 1

            if length > max:
                max = length            

        return max
        
# @lc code=end

