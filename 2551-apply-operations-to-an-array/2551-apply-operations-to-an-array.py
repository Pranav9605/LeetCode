class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)-1):
            if nums[x]==nums[x+1]:
                nums[x]=nums[x]*2
                nums[x+1]=0
        y=0        
        for x in range(len(nums)):
            if nums[x]!=0:
                nums[x],nums[y]=nums[y],nums[x]
                y+=1
        return nums
        