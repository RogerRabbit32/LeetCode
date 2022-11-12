class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 1):
            for j in arr[i + 1:]:
                if arr[i] == j * 2 or arr[i] * 2 == j:
                    return True
        return False