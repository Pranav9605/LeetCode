class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for x in s:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        vals=d.values()
        return len(set(vals))==1
        