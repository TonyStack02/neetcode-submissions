class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 #segnaposto
        left = 0
        right = 0
        for i in range(len(prices)):
            current_profit = prices[i] - prices[left]
            if current_profit >= max_profit:
                max_profit = current_profit
            
            right+=1
            if prices[i] < prices[left]:
                left = i

        return max_profit