class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for x,y in a.items():
            if y>1:
                return True
        return False
        