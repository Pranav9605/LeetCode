class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn=arr[-1]-arr[0]
        out=[]
        for x in range(1,len(arr)):
            minn=min(minn,arr[x]-arr[x-1])
        for x in range(len(arr)-1):
            if arr[x+1]-arr[x] ==minn:
                out.append([arr[x],arr[x+1]])
        return out

                

        