class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        x=str(x)
        bool=True
        for i in range(len(x)/2):
            if x[i]!=x[-i-1]:
                bool=False
                break
        return bool
        """
        :type x: int
        :rtype: bool
        """