class Solution:
    
    # 접근1. 바로떠오르는풀이 dfs
    def sol_1(self, nums):
        
        def dfs(nums, start, curr_nums):
            ans.append(curr_nums[:])
            if len(curr_nums) == len(nums):
                return
            
            for i in range(start, len(nums)):
                val = nums[i]
                if not visited[val]:
                    visited[val] = True
                    curr_nums.append(val)
                    dfs(nums, i + 1, curr_nums)
                    curr_nums.pop()
                    visited[val] = False
        
        ans = []
        visited = dict()
        for elem in nums:
            visited[elem] = False
        
        dfs(nums, 0, [])
        return ans
        
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.sol_1(nums)