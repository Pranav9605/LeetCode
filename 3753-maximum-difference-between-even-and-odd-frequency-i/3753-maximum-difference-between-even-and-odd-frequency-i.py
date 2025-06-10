class Solution:
    def maxDifference(self, s: str) -> int:
        a=[]
        b=[]
        dictt={}
        for x in s:
            if x not in dictt:
                dictt[x]=1
            else:
                dictt[x]+=1
        
        for x,y in dictt.items():
            print(y)
            if y%2==0:
                a.append(y)
            else:
                b.append(y)
        c=max(b)-min(a)
        return c


        