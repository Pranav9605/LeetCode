class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count=0
        a=[0]
        sorted(nums)
        for x in range(len(nums)):
            count+=1
            a.append(count)
        for x in range (len(a)):
            if x not in nums:
                return x

        






        