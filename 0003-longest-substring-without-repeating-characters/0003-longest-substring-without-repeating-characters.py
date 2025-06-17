class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx=0
        for x in range(len(s)):
            seen=set()
            for y in range(x,len(s)):
                if s[y] not in seen:
                    seen.add(s[y])
                    maxx=max(maxx,len(seen))
                else:
                    break
        return maxx



        