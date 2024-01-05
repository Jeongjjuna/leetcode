import heapq

# 행의 약함
# 행의 군인수가 더 적을 경우 약한 행이다.
# 군인수가 같다면, 행번호가 작을경우 더 약한 행이다.

# 가장 약한 k개의 행을 구하여라

# 약한순으로 우선순위를 잡자
# 1순위 -> 군인수가 작은 순
# 2순위 -> 행번호가 작은 순
class Solution:
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        hq = []
        n = len(mat)
        for row in range(n):
            soldiers_cnt = sum(mat[row]) # row 행의 군인 수
            heapq.heappush(hq, (soldiers_cnt, row))# (1순위 : 군인수, 2순위 : 행번호)
        
        
        #  hq = [(1, 2), (2, 0), (2, 3), (4, 1), (5, 4)]
        return [heapq.heappop(hq)[1] for _ in range(k)] # [2,0,3] 출력
        