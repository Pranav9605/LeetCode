class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
            














        # c=len(nums)
        # x=0
        # while x<c:

        #     if nums[x]==0:
        #         nums.append(nums[x])
        #         nums.remove(nums[x])
        #         c-=1
        #         x-=1
        #     x+=1
   
        # return nums
        
        