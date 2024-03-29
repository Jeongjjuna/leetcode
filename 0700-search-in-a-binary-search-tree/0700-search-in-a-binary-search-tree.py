# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sol_1(self, root, val):
        
        def dfs(node):
            nonlocal equals_node
            
            if node == None:
                return
            
            if node.val == val:
                equals_node = node
                return
            
            if node.val < val:
                dfs(node.right)
            elif node.val > val:
                dfs(node.left)
            
            
            
        equals_node = None
        dfs(root)
        return equals_node
        
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.sol_1(root, val)