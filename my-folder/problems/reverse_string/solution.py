class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for x in range(0,len(s)//2):
            temp=s[x]
            s[x]=s[len(s)-1-x]
            s[len(s)-1-x]=temp