class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        print(nums1)
        x=y=0
        out=[]
        while x<len(nums1) and y<len(nums2):
            if nums1[x]<nums2[y]:
                x+=1
            elif nums1[x]>nums2[y]:
                y+=1
            else:
                out.append(nums1[x])
                x+=1
                y+=1
        return out



        