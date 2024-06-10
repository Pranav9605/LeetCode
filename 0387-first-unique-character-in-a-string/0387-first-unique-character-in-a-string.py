class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count the occurrences of each character
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        # Find the first unique character
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        
        return -1




        # for i, char in enumerate(s):
        #     if s.count(char) == 1:
        #         return i
        # return -1


        # count={}
        # for i in s:
        #     if i in count:
        #         count+=1
        #     else:
        #         count=1

        # for x in range (len(s)):
        #     if count[s[x]]==1:
        #         return x
        # return -1
            


        