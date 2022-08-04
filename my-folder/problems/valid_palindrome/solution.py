class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans=""
        for x in range(0,len(s)):
            if s[x]>='a'and s[x]<='z':
                ans=ans+s[x]
            else:
                if s[x] in ['0','1','2','3','4','5','6','7','8','9']:
                    ans=ans+s[x]
        for x in range(0,len(ans)//2):
            if ans[x]!=ans[len(ans)-x-1]:
                return False
        return True