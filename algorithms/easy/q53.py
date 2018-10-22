class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, curr_sum = nums[0], nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],nums[i]+curr_sum)
            max_sum = max(max_sum,curr_sum)
            
        return max_sum