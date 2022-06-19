class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        for x in s:
            flag =False
            while count < len(t):
                if x==t[count]:
                    flag=True
                    count=count+1
                    break
                    
                count=count+1
            if flag!=True:
                return False
        return True
            
                