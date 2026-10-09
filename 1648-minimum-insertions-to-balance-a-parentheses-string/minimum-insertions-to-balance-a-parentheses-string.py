class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        n = 0
        for ch in s:
            if ch == '(':
                n += 2
                if n%2!=0:
                    i +=1
                    n -= 1
            else:
                n-=1
                if n<0:
                    i += 1
                    n = 1
        return i+n
        # stack = []
        # r  = 0
        # i = 0
        # for ch in s:
        #     if ch == '(':
        #         if r == 1:
        #             i += 1
        #             r = 0
        #         stack.append(ch)
        #     else:
        #         r +=1
        #         if stack and r == 2:
        #             stack.pop()
        #             r = 0
        #         elif not stack and r == 2:
        #             i += 1
        #             r = 0

        # i += len(stack) * 2
        # if r == 1:
        #     i += 1
        # return i



        