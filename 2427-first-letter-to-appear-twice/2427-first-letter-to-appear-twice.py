class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                return x

        
        