from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0), (0, 1), (0, -1), (1, 0)]
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        if len(q) == 0:
            return -1
        time = -1
        while q :
            time += 1
            sz = len(q)
            for _ in range(sz):
                x, y = q.popleft()
                for i in range(4):
                    
                    nx = x + dirs[i][0]
                    ny = y + dirs[i][1]
                    if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1):
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx,ny))

        if fresh != 0:
            return -1
        return time    


# time - o(m*n)
# Space - 0(m*n) worst case 
