class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n != 0:
            nums1.pop()
            n -= 1

        count = 0
        while count != len(nums1) and nums2:
            if nums1[count] < nums2[0]:
                    count += 1
            else:
                    nums1.insert(count, nums2[0])
                    nums2.pop(0)
                    count += 1

        if nums2:
            nums1.extend(nums2)