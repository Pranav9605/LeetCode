class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for x in prices[1:]:
            if buy>x:
                buy=x
            profit=max(profit,x-buy)
        return profit



        