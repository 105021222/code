class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs[0]=="":
            return ""
        s=""
        x=1
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                try:
                    if strs[0][i]!=strs[j][i]:
                        x=0
                        break
                except:
                    x=0
                    break
            if x==0:
                break
            else:
                s+=strs[0][i]
        return s
                
                    
                
                       
        """
        :type strs: List[str]
        :rtype: str
        """
        