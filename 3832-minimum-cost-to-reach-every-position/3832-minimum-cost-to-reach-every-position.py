class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        for x in range(1,len(cost)):
            if cost[x]>cost[x-1]:
                cost[x]=cost[x-1]
        return cost

        