class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        
        lenCount = 1
        curr = nums[0]
        idy = 1
        idx = 1
        while idx<len(nums):
            while idy<len(nums) and nums[idy]==curr:
                idy += 1
            if idy>=len(nums):
                break
            lenCount += 1
            curr = nums[idy]
            nums[idx] = curr
            idx += 1
            idy += 1
            
        return lenCount