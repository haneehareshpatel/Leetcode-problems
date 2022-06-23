class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        count=0
        rem_count=0
        ans=list()
        for x in d.keys():
            if int(d[x])%2==0:
                count=count+int(d[x])
            else:
                count=count+((d[x]//2)*2)
                rem_count=rem_count+1
        if rem_count >0:
            return count + 1
        else:
            return count