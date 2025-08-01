class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]
        for _ in range(numRows-1):
            dummy_row=[0] + res[-1] +[0]
            row=[]
            for x in range(len(res[-1])+1):
                row.append(dummy_row[x]+dummy_row[x+1])
            res.append(row)
        return res
        