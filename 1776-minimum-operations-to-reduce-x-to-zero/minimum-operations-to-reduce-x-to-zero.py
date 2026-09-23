class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tar = sum(nums) - x
        n = len(nums)

        if tar < 0:
            return -1
        l, curr = 0, 0
        maxl = -1

        for r in range(n):
            curr+=nums[r]

            while curr > tar:
                curr -= nums[l]
                l+=1
            if curr == tar:
                maxl = max(maxl, r-l+1)
        if maxl == -1:
            return -1
        return n - maxl
        