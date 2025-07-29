class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a=set()
        rev=[]
        for x in range(1,k+1):
            a.add(x)
        for x in range(len(nums)-1,-1,-1):
            rev.append(nums[x])
            if set(rev)>=a: 
                return(len(rev))
            

            
            

        