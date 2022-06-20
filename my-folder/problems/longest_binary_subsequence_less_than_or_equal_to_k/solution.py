import math
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count=0
        n = len(s)-1
        value=0
        while n >= 0:
            if s[n]=='1':
                if (value+math.pow(2,count))<=k:
                    value=value+math.pow(2,count)
                    count+=1
            else:
                count+=1
            n=n-1
        return count
            
                    
                