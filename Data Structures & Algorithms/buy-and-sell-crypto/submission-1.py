class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_p = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_p = max(max_p, profit)
        # return max_p

        l = 0
        profit = 0
        max_p = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[l]:
                l = i
            profit = prices[i] - prices[l]
            max_p = max(max_p, profit)
            
        return max_p

            
        
        
            
        
        