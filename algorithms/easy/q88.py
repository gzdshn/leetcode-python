class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return

        i, j, z = m-1, n-1, len(nums1)-1
        while i >= 0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[z] = nums1[i]
                z -= 1
                i -= 1
            else:
                nums1[z] = nums2[j]
                z -= 1
                j -= 1
        if i<0:
            while z>=0:
                nums1[z] = nums2[j]
                z -= 1
                j -= 1
 