class Solution:
    def maxProfit(self,prices):
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            print(left, right)
            if prices[right] > prices[left]:
                if prices[right] - prices[left] > max_profit:
                    max_profit = prices[right] - prices[left]
            else:
                left = right
            right += 1
        return max_profit
            
    """
    :type prices: List[int]
    :rtype: int
    """
