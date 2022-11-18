class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = {}
        
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        for num in count:
            if count[num] == 1:
                return num
        