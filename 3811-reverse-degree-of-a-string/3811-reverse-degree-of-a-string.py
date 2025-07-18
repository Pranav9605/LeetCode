class Solution:
    def reverseDegree(self, s: str) -> int:
        rev={}
        for x,y in enumerate (string.ascii_lowercase[::-1]):
            rev[y]=x+1
        product=0
        for x,value in enumerate(s):
            product+=(x+1) *rev[value]
            print(value,rev[value])
        return product


            




        