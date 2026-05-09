class Solution(object):
    def maxProfit(self, prices):
        min_prices=prices[0]
        max_profit=0
        for price in prices:
            if price < min_prices:
                min_prices=price
            else:
                profit=price - min_prices
                max_profit=max(max_profit,profit)
        return max_profit
        
        