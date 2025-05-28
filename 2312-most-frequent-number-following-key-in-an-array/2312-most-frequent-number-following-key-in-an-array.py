class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        target={}
        for x in range(len(nums)-1):
            if nums[x]==key:
                if nums[x+1] in target:
                    target[nums[x+1]]+=1
                
                else:
                    target[nums[x+1]]=1
        return max(target, key=lambda k: target[k]) 
        



                

        

        