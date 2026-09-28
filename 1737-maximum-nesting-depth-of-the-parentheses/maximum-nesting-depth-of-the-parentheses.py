class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        maxi = 0
        for ch in s:
            if ch =='(':
                d +=1
                maxi = max(maxi, d)
            elif ch == ')':
                d -= 1
        return maxi