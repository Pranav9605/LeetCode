class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out={}
        for x,y in enumerate(nums):
            diff=target - y
            if diff in out:
                return (out[diff],x)
            out[y]=x



        