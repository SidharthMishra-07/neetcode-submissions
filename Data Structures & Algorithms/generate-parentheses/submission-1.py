class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, stack):
            #Base Case
            if open == close == n:
                res.append("".join(stack))
                return
            if close > open:
                return
            if open < n:
                stack.append('(')
                backtrack(open+1, close, stack)
                stack.pop()
            if close < n:
                stack.append(')')
                backtrack(open, close+1, stack) 
                stack.pop() 

        backtrack(0, 0, [])
        return res
