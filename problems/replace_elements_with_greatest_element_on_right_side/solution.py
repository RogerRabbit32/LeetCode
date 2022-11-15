class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        while index != len(arr) - 1:
            my_max = max(arr[index + 1:])
            arr[index] = my_max
            index += 1
        arr[index] = -1
        return arr