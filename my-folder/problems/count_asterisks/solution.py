class Solution:
    def countAsterisks(self, s: str) -> int:
        if '*' not in s:
            return 0
        flag=False
        count=0
        c_as=0
        for x in range(0,len(s)):
            if s[x]=="|":
                c_as=c_as+1
            if c_as%2==0:
                c_as=0
            if c_as==0:
                if s[x]=="*":
                    count+=1
        return count