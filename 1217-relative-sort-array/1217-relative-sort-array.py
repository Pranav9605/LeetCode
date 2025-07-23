class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}
        last=[]
        first=[]
        for x in arr2:
            dic[x]=0
        for x in arr1:
            if x in dic:
                dic[x]+=1
            else:
                last.append(x)
        last.sort()
        for x in arr2:
            first.extend([x]*dic[x])

        return first+last

        