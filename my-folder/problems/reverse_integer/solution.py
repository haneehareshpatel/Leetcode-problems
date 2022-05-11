import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=""
        flag_neg=False
        if x <0:
            flag_neg=True
            x=-1*x
        
        while x > 0:
            digit = x%10
            num=num+str(digit)
            x=x/10
        if num=="":
            num=0
        else:
            num = int(num)
        if flag_neg:
            num=-1*num
        rang_max = math.pow(2,31)-1
        rang_min = -1*(math.pow(2,31))
        if num > rang_max or num<rang_min:
            num=0
        return num