class Solution:
    
    def dijkstra(self, arr, depth, start, dst, k):
        q = []    
        heapq.heappush(q, (0, start, -1)) # (현재까지 거리, 노드, 거친경유지 개수)
        
        ans = sys.maxsize
        while q:
            dist, now, dep = heapq.heappop(q)

            if now == dst:
                return dist
        
            if dep == k:
                continue
            
            if depth[now] <= dep:
                continue
            
            depth[now] = dep
            
                
        
            for nv, w in arr[now]:
                heapq.heappush(q, (dist + w, nv, dep + 1))

        return ans

    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # 연결그래프 생성
        arr = [[]*n for _ in range(n)]
        for a, b, w in flights:
            arr[a].append((b, w))
        
        
        INF = sys.maxsize
        depth = [INF] * n
        ans = self.dijkstra(arr, depth, src, dst, k)
        
        if ans == sys.maxsize:
            return -1
        return ans