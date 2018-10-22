class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for idy in range(len(nums)):
            if nums[idy]!=val:
                nums[idx] = nums[idy]
                idx += 1
                
        return idx