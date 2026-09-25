class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def p(i):
            res = set()
            curr = {""}
            while i<len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    res |= curr
                    curr = {""}
                    i += 1
                elif expression[i] == '{':
                    sub, i = p(i+1)
                    newcurr = set()
                    for a in curr:
                        for b in sub:
                            newcurr.add(a+b)
                    curr = newcurr
                else:
                    newcurr = set()
                    for w in curr:
                        newcurr.add(w+expression[i])
                    curr = newcurr
                    i+=1
            res |= curr

            if i < len(expression) and expression[i] == "}":
                i+=1
            return res, i
        ans, _ = p(0)
        return sorted(ans)
