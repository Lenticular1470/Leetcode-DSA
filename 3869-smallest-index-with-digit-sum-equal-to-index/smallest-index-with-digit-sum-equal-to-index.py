class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            n = nums[i]
            sumi = 0
            while n!=0:
                x = n % 10
                sumi += x 
                n = n//10
            if sumi == i:
                ans = i
                break
        return ans 

        