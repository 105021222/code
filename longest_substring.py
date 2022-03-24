class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        max=1
        i=2
        while i<=len(s):
            x=0
            for j in range(len(s)-i+1):
                t=s[j:j+i]
                tag=1
                for k in range(i):
                    if t.count(t[k])==1:
                        tag*=1
                    else:
                        tag*=0
                if tag:
                    x=1
                    break
            if x:
                max=i
                i=i+1
                
            else:
                break
        return max
        """
        :type s: str
        :rtype: int
        """