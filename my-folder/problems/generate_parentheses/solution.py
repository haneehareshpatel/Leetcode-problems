class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(left , right , ans):
            if left:
                helper(left-1, right, ans + '(')
            if right>left:
                helper(left, right-1, ans+')')
            if not right:
                res.append(ans)
        helper(n,n,"")
        return res
            
                