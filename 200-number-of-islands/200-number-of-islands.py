class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0  or j >= n or grid[i][j] == "0":
                return
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            grid[i][j] = "0"
            
            for idx in range(4):
                nx, ny = i + dx[idx], j + dy[idx]
                dfs(nx, ny)
            
        m = len(grid)
        n = len(grid[0])
        
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        
        return islands