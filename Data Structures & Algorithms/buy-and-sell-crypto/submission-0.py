class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force
        pro = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                   pro_c = prices[j] - prices[i]
                   pro = max(pro_c, pro)

        return pro