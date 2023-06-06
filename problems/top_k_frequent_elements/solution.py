class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurencies = {}
        for elem in nums:
            if elem not in occurencies:
                occurencies[elem] = 1
            else:
                occurencies[elem] += 1
        sorted_occurencies = sorted(occurencies.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(len(sorted_occurencies)):
            if k == 0:
                return result
            else:
                result.append(sorted_occurencies[i][0])
                k -= 1
        return result
