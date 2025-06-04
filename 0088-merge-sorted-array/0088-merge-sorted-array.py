class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mmid=m-1
        nlast=n-1
        r=m+n-1
        while nlast>=0:
            if mmid >=0 and nums1[mmid]>nums2[nlast]:
                nums1[r]=nums1[mmid]
                mmid-=1
            else:
                nums1[r]=nums2[nlast]
                nlast-=1
            r-=1




        """
        Do not return anything, modify nums1 in-place instead.
        """
        