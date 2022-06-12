class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income<brackets[0][0]:
            total=brackets[0][1]*income/100
            return total
        else:
            total=brackets[0][0]*brackets[0][1]/100
        sumans=brackets[0][0]
        for x in range(1,len(brackets)):
            if (sumans+(brackets[x][0]-brackets[x-1][0]))<income:
                total=total+((brackets[x][0]-brackets[x-1][0])*brackets[x][1]/100)
                sumans=sumans+(brackets[x][0]-brackets[x-1][0])
            else:
                total=total+((income-sumans)*brackets[x][1]/100)
                break
        return total