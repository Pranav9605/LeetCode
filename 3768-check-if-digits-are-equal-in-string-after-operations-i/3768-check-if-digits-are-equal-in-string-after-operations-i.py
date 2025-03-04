class Solution:
    def hasSameDigits(self, s: str) -> bool:


        while len(s)>2:
            a=""
            for x in range(len(s)-1):
                a+=str(((int(s[x])+int(s[x+1])))%10)
            s=a
            print(s)
        return s[0]==s[1]


        #         b=s[x]+s[x+1]%10
        #         a-=1
        # return b[0]==b[1]


        