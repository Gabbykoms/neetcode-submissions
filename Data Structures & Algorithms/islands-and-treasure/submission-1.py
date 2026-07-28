class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #starting from treasures, so we just get every distance in incremental form
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visit = set()

        def addRoom(r, c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])


        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                grid[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
            dist += 1
        

        

        