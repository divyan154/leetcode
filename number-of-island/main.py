class Solution:
    def dfs(self, x, y, grid, visited):
        dirs = [(-1,0), (0,-1), (0, 1), (1, 0)]

        visited[x][y] = True
        for i in range(4):
            nx = x + dirs[i][0]
            ny = y + dirs[i][1]

            if (0 <= nx < self.m and 0 <= ny < self.n and not visited[nx][ny] and grid[nx][ny] == '1'):
                self.dfs(nx, ny, grid, visited)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        cnt = 0
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1' and visited[i][j] == False:
                    self.dfs(i,j, grid, visited)
                    cnt += 1

        return cnt

        