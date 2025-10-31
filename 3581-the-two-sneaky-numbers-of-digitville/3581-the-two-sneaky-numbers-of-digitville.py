class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict={}
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        return list({x for x, count in dict.items() if count>1})
        