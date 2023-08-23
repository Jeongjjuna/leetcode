// 과반수 이상이 되는 숫자 찾기
// 항상 존재한다.
// 선형 시간복잡도 -> 정렬은 쓸 수 없다.

class Solution {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> m = new HashMap<>();
        
        // HashMap에 카운트해서 관리
        for (int num : nums) {
            if(m.containsKey(num)) {
                m.put(num, m.get(num) + 1);
            } else {
                m.put(num, 1);
            }
        }
        
        // 과반수 이상이되는 키값을 찾는다.
        // 과반수 되늰 수가 무조건 존재하므로 바로 return
        for (Map.Entry<Integer, Integer> entry : m.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (value > n/2) {
                return key;
            }
        }
        
        return 0;
    }
}