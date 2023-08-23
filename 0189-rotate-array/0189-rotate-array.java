class Solution {
    Deque<Integer> dq = new ArrayDeque<>();
    
    public void rotate(int[] nums, int k) {
        
        // 회전을 위해 deque자료구조 사용
        for (int num : nums) {
            dq.add(num);
        }

        // k번 반복
        for (int i = 0; i < k; i++) {
            int elem = dq.pollLast();
            dq.addFirst(elem);
        }
        
        // 기존 배열에 넘겨주기
        for (int i = 0; i < nums.length; i++) {
            nums[i] = dq.pollFirst();
        }
        
        
    }
}