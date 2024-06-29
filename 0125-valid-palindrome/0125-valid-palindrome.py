class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s.lower()
        # s.isalpha()
        # b=s[::-1]
        # s=s.replace(' ','')
        # print(s)
        # return True if s==b else False 


        # s1=''
        # for c in s.low 
        s=[i for i in s.lower() if i.isalnum()]
        return s==s[::-1]


