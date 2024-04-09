class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n - 1
        j = m - 1
        p = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[j] > nums2[i]:
                nums1[p] = nums1[j]
                j -= 1
            else:
                nums1[p] = nums2[i]
                i -= 1
            p -= 1
        
        while p >= 0:
            if i < 0 and j >= 0:
                nums1[p] = nums1[j]
                j -= 1
            elif i >= 0 and j < 0:
                nums1[p] = nums2[i]
                i -= 1
            p -= 1
        
        return nums1
