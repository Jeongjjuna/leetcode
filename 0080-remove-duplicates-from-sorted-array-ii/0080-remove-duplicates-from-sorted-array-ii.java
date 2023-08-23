class Solution {
    public int removeDuplicates(int[] nums) {
        
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > nums.length - 3 || nums[i] != nums[i + 2]) {
                nums[idx] = nums[i];
                idx += 1;
            }
        }
        
        return idx;
        
    }
}