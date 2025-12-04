class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        currentMax = 0
        totalMax = 0
        for i in range (1, len(prices)):
            currentMax = max(0, currentMax + prices[i] - prices[i-1])
            totalMax = max(currentMax, totalMax)
        
        return totalMax
        

        