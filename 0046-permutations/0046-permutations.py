import copy

# 순열라이브러리 사용x
class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(nums, visited, ans, curr_num):
            
            if len(nums) == len(curr_num):
                ans.append(copy.deepcopy(curr_num))
                return

            for nv in nums:
                if not visited[nv]:
                    visited[nv] = True
                    curr_num.append(nv)

                    dfs(nums, visited, ans, curr_num)

                    visited[nv] = False
                    curr_num.pop()
        
        
        # --------- 메인 코드 --------------    
        ans = []
        visited = dict()
        for elem in nums:
            visited[elem] = False
            
        dfs(nums, visited, ans, [])
        
        return ans