class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for x in strs:
            count=[0]*26
            for y in x:
                count[ord(y)-ord('a')]+=1
            ans[tuple(count)].append(x)
        return ans.values()