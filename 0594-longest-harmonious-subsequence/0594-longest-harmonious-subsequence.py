class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxx=0
        freq=Counter(nums)
        for x,y in freq.items():
            if x+1 in freq:
                maxx=max(maxx,freq[x]+freq[x+1])
        return maxx



        