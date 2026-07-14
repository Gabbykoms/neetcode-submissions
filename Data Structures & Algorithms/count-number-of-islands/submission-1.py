class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc]== "0"):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
  
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    num_islands += 1
        
        return num_islands
        


        


        
        