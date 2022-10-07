from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def bfs(start_i, start_j):
            q = deque([(start_i, start_j)])
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            while q:
                i, j = q.popleft()
                grid[i][j] = "0"
                
                for idx in range(4):
                    nx, ny = i + dx[idx], j + dy[idx]
                    
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and (nx, ny) not in q:
                        q.append((nx, ny))
                        
        
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    bfs(i, j)
                    
        return islands