class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=len(nums)
        x=0
        while x<c:

            if nums[x]==0:
                nums.append(nums[x])
                nums.remove(nums[x])
                c-=1
                x-=1
            x+=1
   
        return nums
        
        