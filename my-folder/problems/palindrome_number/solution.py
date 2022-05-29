class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = False
        num=x
        count=0
        ans=""
        if num<0:
            num=num*-1
        while num>0:
            res = num%10
            num=num//10
            ans=ans+str(res)
            count+=1
        if ans==str(x):
            return True
        elif x==0:
            return True
        else:
            return False