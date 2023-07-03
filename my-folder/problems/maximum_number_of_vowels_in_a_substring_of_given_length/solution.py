class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        left = 0
        ans = 0
        count = 0
        for i in range(0, len(s)):
            if s[i] in vowels:
                count = count +1
            print(count)
            print("*******")
            while (i-left+1)>k and left <i:
                if s[left] in vowels:
                    print(count)
                    count = count -1
                left = left +1
            
            if (i-left+1)==k:
                ans = max(ans,count)
                print("**********")
                print(count)
                print("*************")
        return ans