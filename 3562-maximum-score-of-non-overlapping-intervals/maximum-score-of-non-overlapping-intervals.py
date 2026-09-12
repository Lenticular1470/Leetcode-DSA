from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        a = []
        for i in range(n):
            a.append([intervals[i][0],intervals[i][1], intervals[i][2], i])
        
        a.sort(key = lambda x: x[1])
        ends = [x[1] for x in a]

        prev = []
        for i in range(n):
            start = a[i][0]
            j = bisect_left(ends, start)

            prev.append(j)

        dp = [[(0, []) for _ in range(5)] for _ in range(n+1)]
        for i in range(1, n+1):
            start, end, weight, index = a[i-1]

            for k in range(1, 5):
                dp[i][k] = dp[i-1][k]

                p = prev[i-1]

                olds, oldi = dp[p][k-1]

                news = olds + weight
                newi = oldi + [index]

                newi.sort()

                if news > dp[i][k][0]:
                    dp[i][k] = (news, newi)
                elif news == dp[i][k][0]:
                    if newi < dp[i][k][1]:
                        dp[i][k] = (news, newi)

        return dp[n][4][1]
                