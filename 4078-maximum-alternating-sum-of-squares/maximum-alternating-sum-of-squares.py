class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort(reverse=True)
        n = len(nums)
        return sum(nums[:(n+1)//2]) - sum(nums[(n+1)//2 :])
                
                