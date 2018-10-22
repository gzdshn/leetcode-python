class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        minLength = float('inf')
        for s in strs:
            if len(s)<minLength:
                minLength = len(s)
            
        pref = ""
        for idx in range(minLength):
            c = strs[0][idx]
            idy = 1
            while idy<len(strs) and strs[idy][idx] == c:
                idy += 1
            if idy==len(strs):
                pref += c
            else: 
                break
        return pref        
        