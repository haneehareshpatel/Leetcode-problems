class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc=Counter(ransomNote)
        mc=Counter(magazine)
        for x in ransomNote:
            if x not in mc.keys():
                return False
            if rc[x] > mc[x]:
                return False
        return True