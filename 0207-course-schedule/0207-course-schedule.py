class Solution:
    
    # 접근1. dfs
    # 아이디어 : 순환되는 그래프가 있는지 체크한다.
    def sol_1(self, numCourses, prerequisites):
        
        def dfs(start, v):
            for nv in graph[v]:
                if start == nv:
                    return True
                
                if not visited[nv]:
                    visited[nv] = True
                    is_cycle = dfs(start, nv)
                    if is_cycle:
                        return True
            return False
                
        # 연결리스트, 모든노드리스트 생성
        graph = [[]*numCourses for _ in range(numCourses)]
        nodes = set()
        for elem in prerequisites:
            a, b = elem[0], elem[1]
            graph[a].append(b)
            nodes.add(a)
            nodes.add(b)
        nodes = list(nodes)
        
        
        # 모든 노드들에 대해 사이클이 있는지 확인한다
        print(nodes, graph)
        for node in nodes:
            visited = {n: False for n in nodes}
            visited[node] = True
            if dfs(node, node):
                return False
        return True

        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.sol_1(numCourses, prerequisites)