class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        max=(len(nums)-1)
        while low<=max:
            mid=(low+max)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]<target:
                    low=mid+1
                else:
                    max=mid-1
        return low


        