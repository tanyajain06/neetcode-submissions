class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # creating sliding window pointers
        left = 0
        right = 1
        # max profit
        maxProfit = 0

        while right < len(prices):
            # check for profitability (btw left and right ptrs)
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                # ensure that this profit is the highest profit possible & update
                # comparing current maxProfit with the newest calculated profit
                maxProfit = max(maxProfit, profit)
            else:
                # updating left pointer to be at new minimum
                # (since right less than left)
                left = right
            # continue updating right ptr until you reach end of prices
            right += 1
        # return maximum profit
        return maxProfit