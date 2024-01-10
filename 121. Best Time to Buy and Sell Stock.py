class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        mx = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]

                mx = max(profit, mx)
            else:
                left = right

            right += 1

        return mx
