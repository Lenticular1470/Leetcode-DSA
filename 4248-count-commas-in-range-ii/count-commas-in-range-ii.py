class Solution:
    def countCommas(self, n: int) -> int:
        a = 0
        sa = 1000
        co = 1
        while sa<=n:
            e = sa*1000 - 1
            c = min(n, e) - sa + 1
            a += c * co
            sa *= 1000
            co += 1
        return a


        