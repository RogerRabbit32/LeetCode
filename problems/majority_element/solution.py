class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        max_key = 0
        max_value = 0

        for key in count.keys():
            if count[key] > max_value:
                max_key = key
                max_value = count[key]

        return max_key
