# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    # 접근1. 아이디어 dfs 분할정복
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
    

    # 접근2. 트리가 아닌 전부 양방향 그래프로 바꿔준다.
    # 그리고 dfs(bfs)후 가장 먼 노드에서 한번더 dfs(bfs)해서 가장 긴 길이를 구한다.
    # 단 주어진 노드들의 노드값이 같을 수 있음 [1, 1, 1, 1, 1]
    # 그러므로 그래프를 만들 때 임의로 중복되지않는 값을 준다. id값처럼
    def sol_2(self, root):
        
        def set_graph(node):
            nonlocal id
            
            if node == None:
                return
            
            if node.left != None:
                node.left.val = id
                id += 1
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right != None:
                node.right.val = id
                id += 1
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                
            set_graph(node.left)
            set_graph(node.right)
        
        
        def dfs(v, dep):
            nonlocal far_node, far_node_dep
            
            if far_node_dep <= dep:
                far_node_dep = dep
                far_node = v
            
            for nv in graph[v]:
                if not visited[nv]:
                    visited[nv] = True
                    dfs(nv, dep + 1)
        
        
        n = 10000
        graph = [[]*(n + 1) for _ in range(n + 1)]
        id = 1
        root.val = id
        id += 1
        set_graph(root)
        # graph = [[], [2, 3], [1, 4, 5], [1], [2], [2], [] ......  
        
        
        # 임이의 점에서 가장 멀리있는 노드를 구한다.
        # 여기서는 1번노드에서 시작했더니, 가장멀리있는 노드 5가 구해졌다.(4가 구해져도 상관없음)
        start = root.val
        far_node, far_node_dep = start, 0
        visited = [False] * (n + 1)
        visited[start] = True
        dfs(start, 0)
        # 출력결과 far_node = 5, far_node_dep = 2
        # print(far_node, far_node_dep)
        
        start = far_node
        far_node, far_node_dep = start, 0
        visited = [False] * (n + 1)
        visited[start] = True
        dfs(start, 0)
        # 출력결과 far_node = 3, far_node_dep = 3
        # print(far_node, far_node_dep)
        
        return far_node_dep
    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.sol_2(root)