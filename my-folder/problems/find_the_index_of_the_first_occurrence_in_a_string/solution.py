class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        count=0
        ctr=0
        temp=0
        flag=True
        while count<len(haystack):
            if ctr<len(needle) and haystack[count]==needle[ctr]:
                if ctr==0:
                    flag=True
                    temp=count
                ctr+=1
            else:
                if ctr!=len(needle):
                    if flag and ctr==len(needle):
                        return temp
                    else:
                        count=count-ctr
                    flag=False
                    ctr=0
                    temp=0
            count+=1
        return temp