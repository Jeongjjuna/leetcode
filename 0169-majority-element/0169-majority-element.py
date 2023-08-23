class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # 최다 요소 구하기.
        count = dict()
        max_value_elem = nums[0]
        max_value = 1
        for elem in nums: #O(n)
            if elem not in count:
                count[elem] = 1
            else:
                count[elem] += 1
                if max_value < count[elem]:
                    max_value = count[elem]
                    max_value_elem = elem

        return max_value_elem