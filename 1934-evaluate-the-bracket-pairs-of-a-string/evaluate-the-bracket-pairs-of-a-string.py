class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        i = 0
        mp = dict(knowledge)
        ans = []
        while i < len(s):
            if s[i] == "(":
                j = i+1
                while s[j] != ")":
                    j += 1
                k = s[i+1 :j]
                ans.append(mp.get(k, '?'))
                i = j+1
            else:
                ans.append(s[i])
                i += 1
        return ''.join(ans)

            




        