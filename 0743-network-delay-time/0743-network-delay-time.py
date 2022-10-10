import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = [[] for _ in range(n + 1)]
        
        for time in times:
            graph[time[0]].append((time[1], time[2]))
            
        inf = int(1e9)
        distance = [inf] * (n + 1)
        distance[k] = 0
        
        h = []
        heapq.heappush(h, (0, k))
        
        while h:
            dist_now, node_now = heapq.heappop(h)
            
            if dist_now > distance[node_now]:
                continue
            
            for node, dist in graph[node_now]:
                cost = dist_now + dist
                
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(h, (cost, node))
                    
        if inf in distance[1:]:
            return -1
        
        return max(distance[1:])