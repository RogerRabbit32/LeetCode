class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        cur_max = 0
        for symbol in nums:
            if symbol == 1:
                cur_max += 1
            else:
                if cur_max > max:
                    max = cur_max
                cur_max = 0
        if cur_max > max:
            max = cur_max
        return max