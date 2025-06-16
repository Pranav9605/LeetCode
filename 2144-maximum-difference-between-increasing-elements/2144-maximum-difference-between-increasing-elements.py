class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff=-1
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                
                if nums[y] > nums[x]:
                    max_diff=max(max_diff,nums[y]-nums[x])
                    print(max_diff)

        return max_diff 

        