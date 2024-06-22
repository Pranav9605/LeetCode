class Solution:
    def splitNum(self, num: int) -> int:
        s=str(num)
        s=sorted(s)
        a,b='',''
        for x in range(len(s)):
            if x % 2==0:
                a+= s[x]
            else:
                b+= s[x]
        return int(a) + int(b)
