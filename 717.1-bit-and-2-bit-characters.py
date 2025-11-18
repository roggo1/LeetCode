#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        answer = True
        for i in range(len(bits) - 1):
            if answer and bits[i] == 1:
                answer = False
            else:
                answer = True
        return answer
# @lc code=end

