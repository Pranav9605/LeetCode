class Solution:
    def maximum69Number (self, num: int) -> int:
        a=str(num)
        i=-1
        for x in range(len(a)):
            if a[x]=='6':
                i=x
                break
        if i ==-1:
            return num
        else:
            return int(a[:i]+'9'+a[i+1:])



        