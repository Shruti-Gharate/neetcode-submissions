class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left= 0
        m_pro = 0
        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                m_pro = max(m_pro, prices[right] - prices[left])
        return m_pro
        #Brute Force      
#        pro = 0
#        for i in range(len(prices)):
#            for j in range(i + 1, len(prices)):
#                   pro_c = prices[j] - prices[i]
#                   pro = max(pro_c, pro)

#        return pro