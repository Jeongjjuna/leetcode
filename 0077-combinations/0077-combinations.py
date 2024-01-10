class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def dfs(start, curr_num, dep, n, k):
            
            if dep == k:
                ans.append(curr_num[:])
                return

            for i in range(start, n + 1):
                if not visited[i]:
                    visited[i] = True
                    curr_num.append(i)

                    dfs(i + 1, curr_num, dep + 1, n, k)

                    visited[i] = False
                    curr_num.pop()
        
        
        # --------- 메인 코드 --------------    
        ans = []
        visited = [False] * (n + 1)
        dfs(1, [], 0, n, k)
        
        return ans