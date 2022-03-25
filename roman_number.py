class Solution(object):
    def romanToInt(self, s):
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=dic[s[-1]]
        for i in range(len(s)-1):
            if dic[s[-2-i]]<dic[s[-1-i]]:
                sum-=dic[s[-2-i]]
            else:
                sum+=dic[s[-2-i]]
        return sum
        """
        :type s: str
        :rtype: int
        """