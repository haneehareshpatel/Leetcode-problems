class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = ""
        carry = 0
        a = int(a)
        b = int(b)
        if a == 0 and b == 0:
            return "0"
        while a > 0 or b > 0 or carry > 0 :
            d1 = a%10
            d2 = b%10
            if d1 + d2 + carry == 2:
                num = num + "0"
                carry=1
            elif d1 + d2 + carry == 3:
                num = num + "1"
                carry=1
            elif d1 + d2 + carry == 1:
                num = num + "1"
                carry=0
            else:
                num = num + "0"
                carry = 0
            a=a//10
            b=b//10
        ans=""
        for i in range (0, len(num)):
            ans=ans+num[len(num)-i-1]
        return ans