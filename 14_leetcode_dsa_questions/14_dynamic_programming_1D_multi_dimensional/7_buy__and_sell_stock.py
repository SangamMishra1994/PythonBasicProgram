from typing import List


class Solution7:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = float("-inf")
        sell = 0

        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell


if __name__ == "__main__":
    prices, fee = [1, 3, 2, 8, 4, 9], 2
    object = Solution7()
    print(f" Best time to buy and sell stock - > "
          f" {object.maxProfit(prices, fee)}")
