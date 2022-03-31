class Solution(object):
    def isValid(self, s):
        if s=="":
            return True
        if len(s)%2==1:
            return False
        dic={"]":"[","}":"{",")":"("}
        stack=[]
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys() and stack!=[]:
                if dic[i]!=stack.pop():
                    return False
            else:
                return False
        if stack!=[]:
            return False
        return True