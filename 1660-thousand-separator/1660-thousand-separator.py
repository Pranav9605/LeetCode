class Solution:
    def thousandSeparator(self, n: int) -> str:
        a=str(n)
        new=""
        count=0
        if len(str(n))<=3:
            return str(n)
        
        for x in range(1,len(a)+1):
            new+=a[-x]               
            count+=1
            if count==3:
                new+="."
                count=0
        
        c=new[::-1]
        if c[0]==".":
            return c[1:]
        return c

       

        