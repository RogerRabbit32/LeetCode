class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for number in nums:
            symbols_count = 0
            for symbol in str(number):
                symbols_count += 1
            if symbols_count % 2 == 0:
                count += 1
        return count