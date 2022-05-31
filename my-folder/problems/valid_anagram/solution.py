class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc=Counter(s)
        tc=Counter(t)
        for x in s:
            if x not in tc.keys():
                return False
            if sc[x]!=tc[x]:
                return False
        for z in t:
            if z not in sc.keys():
                return False
            if sc[x]!=tc[x]:
                return False
        return True