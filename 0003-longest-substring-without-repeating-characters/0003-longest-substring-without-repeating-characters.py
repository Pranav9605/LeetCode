class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        uniq=set()
        max_len=0
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l+=1
            uniq.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len

















        # l=0
        # max_len=0
        # seen=set()
        # for r in range(len(s)):
        #     while s[r] in seen:
        #         seen.remove(s[l])
        #         l+=1
        #     seen.add(s[r])
        #     max_len=max(max_len,r-l+1)
        # return max_len



        