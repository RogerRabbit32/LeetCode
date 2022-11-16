class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i = 0
        while nums1 and nums2 and i!= len(nums1):
            if nums1[i] in nums2:
                x = nums1[i]
                result.append(x)
                nums1.remove(x)
                nums2.remove(x)
            else:
                i += 1
        return result
    