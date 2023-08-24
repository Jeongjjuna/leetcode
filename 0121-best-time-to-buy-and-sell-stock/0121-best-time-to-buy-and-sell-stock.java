class Solution { 
    public int maxProfit(int[] prices) {
            
            int n = prices.length;
            int min_val = prices[0];
            int ans = 0;
            
            for (int i = 1; i < n; i++) {
                ans = Math.max(ans, prices[i] - min_val);
                
                min_val = Math.min(min_val, prices[i]);
            }
            
            return ans;
       
    }
}