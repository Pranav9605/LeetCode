class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        print(*strs)
        for a in zip(*strs):
            print(a)
            if len(set(a)) == 1: 
                res += a[0]
            else: 
                return res
        return res
        