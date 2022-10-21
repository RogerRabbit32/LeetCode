class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for i in sorted(nums):
            if i != count:
                return count
            count += 1
        return count
        