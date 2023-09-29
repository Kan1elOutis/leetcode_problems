# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        stack = []

        def gen_parentheses(openPan, closePan):
            if openPan == closePan == n:
                res.append(''.join(stack))
                return
            if openPan > closePan:
                stack.append(')')
                gen_parentheses(openPan, closePan + 1)
                stack.pop()
            if openPan < n:
                stack.append('(')
                gen_parentheses(openPan + 1, closePan)
                stack.pop()

        gen_parentheses(0, 0)
        return res
