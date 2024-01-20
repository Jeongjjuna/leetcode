class Solution:
    
    
    def dijkstra(self, arr, distance, start):
        q = []    
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)

            if distance[now] != dist:
                continue

            for nv, w in arr[now]:
                if dist + w < distance[nv]:
                    distance[nv] = dist + w
                    heapq.heappush(q, (dist + w, nv))
    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 연결그래프  생성
        arr = [[]*(n + 1) for _ in range(n + 1)]
        for a, b, w in times:
            arr[a].append((b, w))

        # 다익스트라
        INF = sys.maxsize
        distance = [INF] * (n + 1)
        self.dijkstra(arr, distance, k)
        
        
        # 
        ans = 0
        for i in range(1, n + 1):
            if distance[i] == INF:
                return -1
            
            ans = max(ans, distance[i])
        
        
        return ans
        

        