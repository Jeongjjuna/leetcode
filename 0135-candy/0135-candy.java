class Solution {
    
    private List<int[]> priority = new ArrayList<>();
    private int[] candy;
    
    private void compareLeft(int r, int i, int[] ratings) {
        if (r > ratings[i + 1] && candy[i] <= candy[i + 1]) {
            candy[i] = candy[i + 1] + 1;
        }       
    }
    
    private void compareRight(int r, int i, int[] ratings) {
        if (r > ratings[i - 1] && candy[i] <= candy[i - 1]) {
            candy[i] = candy[i - 1] + 1;
        }
    }       
    
    public int candy(int[] ratings) {
        // 방법 : 그리디 -> 낮은 우선부터 사탕 쌓기
            
        // 사탕관리하기
        int n = ratings.length;
        candy = new int[n];
        for(int i = 0; i < n; i++) {
            candy[i] = 1;
        }
        
        // 우선순위 뽑아내기
        for (int i = 0; i < ratings.length; i++) {
            priority.add(new int[]{ratings[i], i});
        }
        Collections.sort(priority, (a, b) -> Integer.compare(a[0], b[0]));

        
        // 사탕이 1개밖에없으면 그냥 끝내기
        if (n == 1) {
            return 1;
        }
            
        
        // 우선순위에 따라 사탕지급
        for (int[] pair : priority) {
            int r = pair[0];
            int i = pair[1];
            
            if (i == 0) {
                compareLeft(r, i, ratings);
            } else if(i == n - 1) {
                compareRight(r, i, ratings);
            } else {
                compareLeft(r, i, ratings);
                compareRight(r, i, ratings);
            }
        }
            
                    
        return Arrays.stream(candy).sum();
    }
}