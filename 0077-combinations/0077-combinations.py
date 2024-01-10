class Solution:
    # 접근1. dfs
    def sol_1(self, n, k):
                
        def dfs(start, n, k, dep, curr_num):
            if dep == k:
                ans.append(curr_num[:])
                return

            for i in range(start, n + 1):
                if not visited[i]:
                    # 1. 방문처리, 값 넣기
                    visited[i] = True
                    curr_num.append(i)

                    # 2. dfs
                    dfs(i + 1, n, k, dep + 1, curr_num)
                    
                    # 3. 방문처리 풀기, 값빼기
                    visited[i] = False
                    curr_num.pop()
        
        
        # --------- 메인 코드 --------------    
        ans = []
        visited = [False] * (n + 1)
        start, dep, curr_num = 1, 0, []
        dfs(start, n, k, dep, curr_num)
        
        return ans
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.sol_1(n, k)
