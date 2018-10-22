class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        idx = 0
        digits[idx] += 1
        if digits[idx]<10:
            return digits[::-1]
        
        while digits[idx]>9:
            digits[idx] = 0
            idx += 1
            if idx==len(digits):
                digits.append(1)
                return digits[::-1]
            digits[idx] += 1
        
        return digits[::-1]