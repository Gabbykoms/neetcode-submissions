class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r,c)])
            visit = [[False]* COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    if grid[r][c] == 0:
                        return steps
                
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROWS and  0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc]!= -1 ):
                            visit[nr][nc] = True
                            q.append((nr, nc))
                steps +=1
            return INF
                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        