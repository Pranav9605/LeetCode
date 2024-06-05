class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        for x in range(0,len(nums),2):
            nums[x],nums[x+1]=nums[x+1],nums[x]
            
        return nums

        



        
        