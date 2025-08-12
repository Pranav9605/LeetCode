class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        l=[]
        sor=sorted(divisors)
        for x  in sor:
            c=0
            for y in nums:
                if y%x==0:
                    c+=1
            l.append(c)
        return sor[l.index(max(l))]
        