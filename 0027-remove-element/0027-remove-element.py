class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[k] = nums[x]
                k+=1
        return k


        # val=0
        # for x in nums:
        #     if x in nums:
        #         val=x
        #         nums.pop(x)
        # return val


            
                
        