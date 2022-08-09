class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=0
        finalstr=""
        for i in range(0,len(s)):
            left , right = i, i
            
            while left >=0 and right <len(s) and s[left]==s[right]:
                if res<(right-left+1):
                    finalstr=s[left:right+1]
                    res=right-left+1
                left-=1
                right+=1
                
            left , right = i, i+1
            
            while left>=0 and right < len(s) and s[left]==s[right]:
                if res < (right-left+1):
                    finalstr=s[left:right+1]
                    res=right-left+1
                left-=1
                right+=1
                
        return finalstr