class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_set = set()
        
        for i, num in enumerate(nums):
            if num in num_set:
                return True
            
            num_set.add(num)
            
            if len(num_set) > k:
                num_set.remove(nums[i - k])
        
        return False



        # for i in range (len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and abs(i - j) <= k:
        #             return True
                    

        # return False


        