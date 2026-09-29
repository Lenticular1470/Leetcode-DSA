class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)                
        n = len(grid[0])
        if(m+n-1) % 2 != 0:
            return False
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    if grid[i][j] == '(':
                        dp[j].add(1)
                    continue
                new_b = set()
                if i > 0:
                    new_b.update(dp[j])
                if j > 0:
                    new_b.update(dp[j-1])
                dp[j] = set()
                for b in new_b:
                    if grid[i][j] == '(':
                        nb = b + 1
                    else:
                        nb = b - 1
                    if nb >= 0:
                        dp[j].add(nb)
        return 0 in dp[n-1]
