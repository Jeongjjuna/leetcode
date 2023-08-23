class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 중복 요소를 모두 제거하기
        s = set()
        for elem in nums:
            s.add(elem)
            
        
        idx = 0
        non_duplicate_nums = list(s)
        non_duplicate_nums.sort()
        for x in non_duplicate_nums:
            nums[idx] = x
            idx += 1
            
        return len(s)