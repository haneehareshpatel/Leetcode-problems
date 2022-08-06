class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        result=0
        anset= set()
        for right in range(0,len(s)):
            
            while s[right] in anset:
                anset.remove(s[left])
                left+=1
            anset.add(s[right])
            result=max(result,right-left+1)
        return result