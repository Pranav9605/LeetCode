class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        return num==int(str(int(str(num)[::-1]))[::-1]) 


        # a=str(num)[::-1]
        # a=int(a)
        # a=str(a)
        # a=a[::-1]
        # a=int(a)

        # return True if num==a else False
        