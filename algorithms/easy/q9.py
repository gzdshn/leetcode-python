class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10==0 and x!=0):
            return False
            
        halfReverse = 0
        while x>halfReverse:
            halfReverse = halfReverse*10 + x%10
            x /= 10
        
        return (x == halfReverse) or (x == halfReverse/10)