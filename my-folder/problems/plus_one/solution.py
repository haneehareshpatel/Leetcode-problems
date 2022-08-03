class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]=digits[-1]+1
        else:
            flag=True
            ctr=len(digits)-1
            carry=0
            while flag and ctr>=0:
                if ctr==len(digits)-1:
                    digits[ctr]=digits[ctr]+1+carry
                else:
                    digits[ctr]=digits[ctr]+carry
                if digits[ctr]>9:
                    carry=digits[ctr]//10
                    digits[ctr]=digits[ctr]%10
                else:
                    carry=0
                    flag=False
                ctr-=1
            if carry!=0:
                digits.insert(0,carry)
        return digits