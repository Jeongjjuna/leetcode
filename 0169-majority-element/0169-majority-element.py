# 과반수 이상이 되는 숫자 찾기
# 항상 존재한다.
# 선형 시간복잡도 -> 정렬은 쓸 수 없다.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
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
        

        