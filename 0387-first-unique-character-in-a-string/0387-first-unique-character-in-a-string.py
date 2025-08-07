class Solution:
    def firstUniqChar(self, s: str) -> int:
        a=Counter(s)
        print(a)
        for x in range(len(s)):
            if a[s[x]]==1:
                return x
        return -1


        