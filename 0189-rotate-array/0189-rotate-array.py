class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       
    
        d = dict()
        n = len(nums)
        
        # k번 이후에 위치할 index를 key, 그 값을 value로 하여 dict에 저장한다.
        for i in range(n): # O(N)
            d[(i + k) % n] = nums[i]
            
        
        for i in range(n): # O(N)
            nums[i] = d[i]