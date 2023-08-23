// class Solution {
//     public int removeDuplicates(int[] nums) {
        
//         int idx = 0;
//         for (int i = 0; i < nums.length; i++) {
//             if (i > nums.length - 3 || nums[i] != nums[i + 2]) {
//                 nums[idx] = nums[i];
//                 idx += 1;
//             }
//         }
        
//         return idx;
        
//     }
// }

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }

        int index = 2;

        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[index - 2]) {
                nums[index] = nums[i];
                index++;
            }
        }

        return index;
    }
}