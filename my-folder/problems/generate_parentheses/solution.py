class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = "("
        ans_list = []
        open = 1
        def rec(ans, open, close):
            if len(ans) < 2*n:
                if ans[-1] == '(':
                    if open < n:
                        rec(ans + '(', open+1,close)
                    if close < n:
                        rec(ans + ')', open, close+1)
                if ans[-1] == ')':
                    if open > close and close <n:
                        rec(ans + ')', open, close+1)
                    if open < n:
                        rec(ans+'(', open+1, close)
            else:
                ans_list.append(ans)
        rec("(",1,0)
        return ans_list