class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        best = 0
        for num in prices:
            if num < low:
                low = num
            if num - low > best:
                best = num - low
        return best