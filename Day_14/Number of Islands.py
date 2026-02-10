class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # stop conditions
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return

            # mark land as visited
            grid[r][c] = "0"

            # visit neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # traverse the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1     # found a new island
                    dfs(i, j)        # visit whole island

        return islands
