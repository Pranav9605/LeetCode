class Solution:
    def modifyString(self, s: str) -> str:
        a=list(s)
        for x in range(len(a)):
            if a[x]=="?":
                for y in "abcdefghijklmnopqrstuvwxyz":
                    if(x==0 or a[x-1]!=y) and (x+1==len(a)or a[x+1] !=y):
                        a[x]=y
        return "".join(a)
                    



        