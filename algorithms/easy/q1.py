class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = dict()
        for idx in range(len(nums)):
            numsDict[nums[idx]] = idx
        for idx in range(len(nums)):
            if (target - nums[idx]) in numsDict and idx != numsDict[(target - nums[idx])]:
                return [idx,numsDict[target - nums[idx]]]