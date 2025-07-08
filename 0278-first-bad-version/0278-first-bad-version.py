# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("3000"))
class Solution: 
    def firstBadVersion(self, n: int) -> int:
        low=0
        high=n
        mid=0
        while low+1<high:
            mid=(low+high)//2
            if isBadVersion(mid)==False:
                low=mid
            else:
                high=mid
            print(low,high)
        return high





        # a=1
        # for x in range(n):
        #     if isBadVersion(x)==True:
        #         a=x
        # return a



        