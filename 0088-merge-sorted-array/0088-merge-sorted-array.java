class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        ArrayList<Integer> result = new ArrayList<>();
        int p1 = 0, p2 = 0;
        
        
        while (p1 < m && p2 < n) {
            if (nums1[p1] <= nums2[p2]) {
                result.add(nums1[p1]);
                p1 += 1;
            } else if(nums1[p1] > nums2[p2]) {
                result.add(nums2[p2]);
                p2 += 1;
            }
        }
        
        // 왼쪽이 남은 경우
        if (p2 == n) {
            while (p1 < m) {
                result.add(nums1[p1]);
                p1 += 1;
            }
            
        // 오른쪽이 남은 경우
        } else if (p1 == m) {
            while (p2 < n) {
                result.add(nums2[p2]);
                p2 += 1;
            }
        }
        
        
        for (int i = 0; i < m + n; i++) {
            nums1[i] = result.get(i);
        }
        
    }
}