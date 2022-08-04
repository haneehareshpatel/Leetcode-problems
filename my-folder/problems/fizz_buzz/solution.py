class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=list()
        for x in range(0,n):
            if (x+1)%3==0 and (x+1)%5==0:
                ans.append("FizzBuzz")
            elif (x+1)%3==0:
                ans.append("Fizz")
            elif (x+1)%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(x+1))
        return ans