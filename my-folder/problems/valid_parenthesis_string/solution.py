class Solution:
    def checkValidString(self, s: str) -> bool:
        maxleft, minleft = 0,0
        for i in range(0,len(s)):
            if s[i]=="(":
                maxleft = maxleft + 1
                minleft = minleft + 1
            if s[i]==")":
                maxleft = maxleft -1
                minleft = minleft -1
            if s[i]=="*":
                maxleft = maxleft+1
                minleft = minleft-1
            if minleft < 0:
                minleft = 0
            if maxleft < 0:
                return False
        if minleft > 0:
            return False
        return True