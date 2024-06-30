class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        mi=min(a,b)
        for x in range(1,mi+1):
            if a%x==0 and b%x==0:
                count+=1
        return count
        