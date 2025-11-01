class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        max_freq=max(c.values())
        return sum(y for x,y in c.items() if y==max_freq)

        
        