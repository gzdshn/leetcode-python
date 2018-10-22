class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        S = s.split()
        if len(S)>0:
            return len(S[-1])
        else:
            return 0