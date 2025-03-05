class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>1 or "LLL" in s:
            return False
        return True
        
        
        
        
        
        
        
        
        
        
        # a={"A":0,"L":0}
        # for x in s:
        #     if x not in a:
        #         a[x]=1
        #     else:
        #         a[x]+=1
        # if a["A"]<2 and a["L"]<3:
        #     return True
        # else:
        #     return False
        # print(a)
         

        