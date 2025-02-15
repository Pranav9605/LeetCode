class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total=[]
        for x in accounts:
            total.append(sum(x))
        # print(total)
        return(max(total))
        