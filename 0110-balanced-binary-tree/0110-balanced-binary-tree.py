# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # dfs로 깊이를 추적한다. -> 분할정복
    def sol_1(self, root):
        
        def dfs(node, dep):
            nonlocal is_balanced
            
            if node == None:
                return 0
            
           
            left_longest_dep = dfs(node.left, dep + 1)
            right_longest_dep = dfs(node.right, dep + 1)
            
            # 왼쪽서브트리 깊이와 오른쪽서브트리 깊이차이가 1초과라면 불균형이다.
            if 1 < abs(left_longest_dep - right_longest_dep):
                is_balanced = False
           
            return max(left_longest_dep, right_longest_dep) + 1
        
        
        is_balanced = True
        dfs(root, 0)
            

        return is_balanced
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.sol_1(root)