class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick(nums):
            if len(nums)<=1:
                return nums
            pivot=random.choice(nums)
            left=[x for x in nums if x<pivot]
            middle = [x for x in nums if x == pivot]
            right=[x for x in nums if x>pivot]
            return quick(left)+middle+quick(right)
        return quick(nums)


















        # def merge(nums):
        #     if len(nums)==1:
        #         return nums
        #     mid=len(nums)//2
        #     left=merge(nums[:mid])
        #     right=merge(nums[mid:])
        #     return sort(left,right)
        # def sort(left,right):
        #     l=r=0
        #     result=[]
        #     while l<len(left) and r<len(right):
        #         if left[l]<right[r]:
        #             result.append(left[l])
        #             l+=1
        #         else:
        #             result.append(right[r])
        #             r+=1
        #     result.extend(left[l:])
        #     result.extend(right[r:])
        #     return result
        # a=merge(nums)
        # return a
        