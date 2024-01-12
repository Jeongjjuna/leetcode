# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    
    # 아이디어 dfs 분할정복
    def sol_1(self, root):

        def dfs(node, dep):
            nonlocal longest
            
            if node == None:
                return -1
            
            # 왼쪽 서브트리중 가장 긴 길이
            left_longest = dfs(node.left, dep + 1)
            right_longest = dfs(node.right, dep + 1)

            # 현재 좌우를 잇는 길이가 최대라면 갱신한다
            longest = max(longest, left_longest + right_longest + 2)
            
            # 반환할 때에는 좌/우중 더긴 값을 기준으로 반환한다.
            return max(left_longest, right_longest) + 1
        
        

        longest = 0
        dfs(root, 0)
            
        
        return longest
        
        
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.sol_1(root)