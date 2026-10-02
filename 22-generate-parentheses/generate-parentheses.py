class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def bk(s, o_c, c_c):
            if len(s) == 2 * n:
                res.append(s)
                return
            if o_c < n:
                bk(s+"(", o_c + 1,  c_c)
            if c_c < o_c:
                bk(s+")", o_c, c_c+1)
        bk("", 0, 0)

        return res