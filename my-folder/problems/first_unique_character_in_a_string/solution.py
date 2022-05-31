class Solution:
    def firstUniqChar(self, s: str) -> int:
        for x in range(0,len(s)):
            if s[x] not in s[x+1:] and s[x] not in s[0:x]:
                return x
        return -1