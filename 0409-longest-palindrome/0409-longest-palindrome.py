class Solution:
    def longestPalindrome(self, s: str) -> int:
        # counts=counter(s)
        # length=0
        # odd_found=False
        # for count in counts.values():
        #     length+=count if count%2==0 else count-1
        #     if count% 2==1:
        #         odd_found=True
        # return length +1 if odd_found else length



        ss=set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss)!=0:
            return len(s)-len(ss)+1
        else:
            return len(s)
        






















        