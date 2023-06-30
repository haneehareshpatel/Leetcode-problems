class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        len1 = len(word1)
        len2 = len(word2)
        lenmin = min(len1, len2)
        for i in range(0, lenmin):
            ans = ans + word1[i]
            ans = ans + word2[i]
        if len1 > len2:
            ans = ans + word1[len2:]
        else:
            ans = ans + word2[len1:]
        return ans