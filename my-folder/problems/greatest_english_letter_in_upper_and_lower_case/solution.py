class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = Counter(s)
        max_letter = 0
        letter = ""
        for x in ans.keys():
            if max_letter < ord(x) and x.upper() in ans.keys() and x.lower() in ans.keys():
                max_letter = ord(x)
                letter = x
        return letter.upper()