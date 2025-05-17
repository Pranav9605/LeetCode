class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while len(nums)>len(set(nums)):
            nums=nums[3:]
            count+=1
        return count









        # for x in range (len(nums)):
        #     if len(nums)!=set(nums):
        #         nums=nums[:x]+nums[x+3:]
        #         x=0
        #         print(nums)




        