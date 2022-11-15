class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for number in nums:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        return even + odd