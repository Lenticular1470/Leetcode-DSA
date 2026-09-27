class Solution:
    def reverseParentheses(self, s: str) -> str:
        # str1 = str()
        # str2  = str()
        # str3 = str()
        # i = 0
        # b = 0
        # while i < len(s):
        #     if s[i] == '(' or b == 1:
        #         b +=1
        #         i = i+1
        #         str3.append(reversed(s[i]))
        #     elif b>1:
        #         str2.append(s[i])
        #         i += 1
        # j = len(n)-1 
        # b = 0
        # while j >=0:
        #     if s[j] == ')' or b == 1:
        #         j -= 1
        #         b += 1
        #         str1.append(s[j])
        #     if b > 1 and s[j] == ")" or s[j] == "(":
        #         break
        # return *(str1+str2+str3)
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()

                for c in temp:
                    stack.append(c)
            else:
                stack.append(ch)
        return ''.join(stack)
            


        