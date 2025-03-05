class Solution:
    def firstUniqChar(self, s: str) -> int:
        a={}
        for x in s:
            if x not in a:
                a[x]=1
            else:
                a[x]+=1
        for x in a:
            if a[x]==1:
                return s.index(x)
            
        return -1
        