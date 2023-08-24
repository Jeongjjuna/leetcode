class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 회전을 위해 deque자료구조 사용
        dq = deque()
        
        for num in nums:
            dq.append(num)

        # k번 반복
        for i in range(k):
            dq.appendleft(dq.pop()) 
            
        # 기존 배열에 넘겨주기
        for i in range(len(nums)):
            nums[i] = dq[i]
        
        