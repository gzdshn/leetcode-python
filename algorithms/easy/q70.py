class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n==1:
            return 1
        dp_array = [0] * (n+1)
        dp_array[1] = 1
        dp_array[2] = 2
        for idx in range(3,n+1):
            dp_array[idx] = dp_array[idx-1] + dp_array[idx-2]  

        return dp_array[n]