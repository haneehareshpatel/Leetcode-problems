class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        anss=list()
        anst=list()
        for x in range(0,len(s)):
            if s[x]!='#':
                anss.append(s[x])
            elif len(anss)>0:
                anss.pop()
            else:
                pass
        for z in range(0,len(t)):
            if t[z]!='#':
                anst.append(t[z])
            elif len(anst)>0:
                anst.pop()
            else:
                pass
        if anss==anst:
            return True
        else:
            return False
        