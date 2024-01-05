import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 행의 약함
        # 행의 군인수가 더 적을 경우 약한 행이다.
        # 군인수가 같다면, 행번호가 작을경우 더 약한 행이다.
        
        # 가장 약한 k개의 행을 구하여라
        
        # 약한순으로 우선순위를 잡자
        # 1순위 -> 군인수가 작은 순
        # 2순위 -> 행번호가 작은 순
        
        
        # row행의 솔져 개수를 구한다.
        def count_soldier(mat, row):
            m = len(mat[row])
            cnt = 0
            for col in range(m):
                if mat[row][col] == 1:
                    cnt += 1
            return cnt
        
        hq = []
        n = len(mat)
        for row in range(n):
            soldiers_cnt = count_soldier(mat, row)
            
            heapq.heappush(hq, (soldiers_cnt, row))
            
            
        answer = []
        for _ in range(k):
            _, weakest = heapq.heappop(hq)
            answer.append(weakest)
            
            
        return answer