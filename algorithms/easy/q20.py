class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chDict = {'}':'{',']':'[',')':'('}
        stck = []
        for ch in s:
            if ch in "({[":
                stck.append(ch)
            else:
                if stck and stck[-1] == chDict[ch]:
                    stck.pop()
                else:
                    return False
        return True if not stck else False