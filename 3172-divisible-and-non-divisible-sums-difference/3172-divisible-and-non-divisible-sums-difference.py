class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1=0
        nums2=0
        for x in range(1,n+1):
            if x%m==0:
                nums1+=x
            else:
                nums2+=x
        return nums2-nums1
        