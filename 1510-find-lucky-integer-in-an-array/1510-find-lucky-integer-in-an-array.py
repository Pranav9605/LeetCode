class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=Counter(arr)
        curr=-1
        for x,y in a.items():
            if x==y:
                curr=max(curr,x)
        return curr





        # dictt={}
        # for x in arr:
        #     if x not in dictt:
        #         dictt[x]=1
        #     else:
        #         dictt[x]+=1
        # for x,y in dictt.items():
            
        
        