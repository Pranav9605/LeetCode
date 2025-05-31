class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(1,len(nums)+1):
            print(x)
            count=0
            for y in nums:
                if y>=x:
                    count+=1
            if count == x:
                return x
        else:
            return -1


            print(x)


        