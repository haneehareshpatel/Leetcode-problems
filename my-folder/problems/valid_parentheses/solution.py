class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag=True
        stack_ans = list()
        stack_ans.append(s[0])
        
        for x in range(1,len(s)):
            if s[x] == '[' or s[x]=='{' or s[x]=='(':
                stack_ans.append(s[x])
            else: 
                if len(stack_ans)>0:
                    if s[x]==']' and stack_ans[-1]!='[':
                        flag=False
                        break
                    elif s[x]=='}' and stack_ans[-1]!='{':
                        flag=False
                        break
                    elif s[x]==')' and stack_ans[-1]!='(':
                        flag=False
                        break
                    else:
                        stack_ans.pop()
                else:
                    stack_ans.append(s[x])
        if len(stack_ans)!=0:
            flag=False
        return flag
            