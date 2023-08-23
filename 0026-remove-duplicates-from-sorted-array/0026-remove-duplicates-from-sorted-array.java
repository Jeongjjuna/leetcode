class Solution {
    public int removeDuplicates(int[] nums) {
        
        HashSet<Integer> s = new HashSet<>();
        for (int num : nums) {
            s.add(num);
        }
        
        ArrayList<Integer> arr_nums = new ArrayList<>(s);
        Collections.sort(arr_nums);
        
        
        for (int i = 0; i < arr_nums.size(); i++) {
            nums[i] = arr_nums.get(i);
        }
        
        return arr_nums.size();
    }
}