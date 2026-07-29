class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0] ]
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1


        