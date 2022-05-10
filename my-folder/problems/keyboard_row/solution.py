class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        ans_lst = list()
        
        for x in words:
            flag_include = False
            f_f=True
            f_s=True
            f_t=True
            for index in x:
                index=index.lower()
                if index in first_row and f_f:
                    flag_include=True
                    f_s=f_t=False   
                elif index in second_row and f_s:
                    flag_include=True
                    f_f=f_t=False
                elif index in third_row and f_t:
                    flag_include=True
                    f_s=f_f=False
                else:
                    flag_include=False
                    break
                    
            if flag_include:
                ans_lst.append(x)
        return ans_lst
                