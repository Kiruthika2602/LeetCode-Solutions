class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low = prices[0]
        profit = 0
        for num in prices:
            if num < low:
                low = num
            diff = num - low
            if diff >= profit:
                profit = diff
        return profit        
