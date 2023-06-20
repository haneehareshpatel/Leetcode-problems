class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        flag = False
        s1 = set(s)
        p1 = set(pattern)
        if len(s1)!=len(p1):
            return False
        
        if len(s)!=len(pattern):
            return False
        for i in range(0, len(pattern)//2+1):
            if pattern[i]==pattern[len(pattern)-i-1]:
                if s[i]!=s[len(s)-1-i]:
                    return False
            if pattern[i]!=pattern[len(pattern)-i-1]:
                if s[i]==s[len(s)-1-i]:
                    return False
            if i-1>=0 and pattern[i]==pattern[i-1]:
                if i-1 >= 0 and s[i]!=s[i-1]:
                    return False
            if i-1>=0 and pattern[i]!=pattern[i-1]:
                if i-1>=0 and s[i]==s[i-1]:
                    return False
        return True