class Solution:
    def canAliceWin(self, n: int) -> bool:
        a=10
        count=0
        while n>=a>0:
            n-=a
            a-=1
            count+=1
        return True if count%2==1 else False
