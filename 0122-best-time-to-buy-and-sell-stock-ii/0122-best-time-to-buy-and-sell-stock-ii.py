class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 값이 오르다가 최대점이 찍힐 때 판다?
        
        n = len(prices)
        min_val = prices[0]
        ans = 0
        for i in range(1, n):
            # 계속 상승중이라면 넘어간다.
            if prices[i - 1] < prices[i]:
                continue
                
            # 상승세가 끊긴다면 i - 1부분이 최대치이다.
            if prices[i - 1] > prices[i]:
                ans += prices[i - 1] - min_val
                min_val = prices[i]
        
        ans += prices[n - 1] - min_val
                
        return ans