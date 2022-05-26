import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        num=n
        while num>=1:
            x=num%2
            if x==1:
                count+=1
            num=math.floor(num/2)
        return count