class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque
        if not heights or len(heights) == 0:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        atl_reach, pac_reach = set(), set()
        atl_q, pac_q = deque(), deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            pac_q.append((r, 0))
            pac_reach.add((r, 0))

            atl_q.append((r, COLS-1))
            atl_reach.add((r, COLS-1))
        
        for c in range(COLS):
            pac_q.append((0, c))
            pac_reach.add((0, c))

            atl_q.append((ROWS-1, c))
            atl_reach.add((ROWS-1, c))
        
        def bfs(queue, reachable):
            while queue:
                row, col = queue.popleft()
                for x, y in directions:
                    dr, dc = row + x, col + y
                    if (dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS or (dr, dc) in reachable):
                        continue
                    if heights[dr][dc] < heights[row][col]:
                        continue
                    reachable.add((dr, dc))
                    queue.append((dr, dc))
            return reachable
        
        pac_reach = bfs(pac_q, pac_reach)
        atl_reach = bfs(atl_q, atl_reach)

        return [[r, c] for r, c, in pac_reach & atl_reach]



        
        
        