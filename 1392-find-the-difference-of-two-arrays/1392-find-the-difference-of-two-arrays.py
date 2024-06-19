class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        out=[]
        out1=[]
        new=[out,out1]
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        for x in nums1:
            if x not in nums2:
                out.append(x)
        for y in nums2:
            if y not in nums1:
                out1.append(y)
        return new



        