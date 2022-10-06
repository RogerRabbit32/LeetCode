class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prom = sorted(nums)
        i, j = 0, len(nums) -1
        while i != j:
            if prom[i] + prom[j] > target:
                j -= 1
            elif prom[i] + prom[j] < target:
                i += 1
            else:
                break
                
        if prom[i] == prom[j]:
            return [nums.index(prom[i]), nums.index(prom[j], nums.index(prom[j]) + 1)]
        else:
            return [nums.index(prom[i]), nums.index(prom[j])]