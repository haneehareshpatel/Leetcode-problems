class Solution:
    def maxProduct(self, words: List[str]) -> int:  
        maxcommon=0
        for x in range(0,len(words)):
            for z in range(x+1,len(words)):
                flag=False
                for w in words[x]:
                    if w in words[z]:
                        flag=True
                if not flag:        
                    temp=len(words[x])*len(words[z])
                    if temp > maxcommon:
                        maxcommon=temp
        return maxcommon