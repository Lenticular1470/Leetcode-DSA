class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0]*k
        for n in nums:
            new = [0] *k
            new[n%k]  += 1
            for r in range(k):
                new[(r*n) % k] += dp[r]

            for r in range(k):
                ans[r] += new[r]
            dp = new
        return ans

        