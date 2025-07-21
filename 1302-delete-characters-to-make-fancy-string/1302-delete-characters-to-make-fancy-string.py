class Solution:
    def makeFancyString(self, s: str) -> str:
        res=''
        cnt=0
        for x in range(len(s)):
            if s[x]==s[x-1]:
                cnt+=1
            else:
                cnt=1
            if cnt<3:
                res+=s[x]
        return res










        