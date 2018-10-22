class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negX = True if x<0 else False
        w = str(abs(x))
        reverse = int(w[::-1])
        if reverse>((2**31)-1):
            return 0
        return -1*reverse if negX else reverse