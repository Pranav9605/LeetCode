class Solution:
    def largestGoodInteger(self, num: str) -> str:
        lst=[]
        for x in range(len(num)-2):
            if num[x]==num[x+1]==num[x+2]:
                a=(num[x]+num[x+1]+num[x+2])
                lst.append(a)
        return max(lst) if lst else ''

        