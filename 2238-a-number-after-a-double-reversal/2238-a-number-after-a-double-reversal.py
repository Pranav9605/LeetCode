class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a=str(num)[::-1]
        a=int(a)
        a=str(a)
        a=a[::-1]
        a=int(a)

        return True if num==a else False
        