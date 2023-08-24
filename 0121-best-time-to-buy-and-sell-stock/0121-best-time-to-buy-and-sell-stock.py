class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 현재 위치를 파는 값이라고 했을 때 지금까지 거쳐온 값들중 가장 싼값과 비교한다.
        
        n = len(prices)
        min_val = prices[0]
        ans = 0
        for i in range(1, n):
            # index 0 ~ i - 1까지 값들 중 가장 작은 값과 비교한다.
            ans = max(ans, prices[i] - min_val)
            
            # 지금까지 들어온 값들 중 가장 작은 값을 갱신한다.
            min_val = min(min_val, prices[i])
            
        return ans