class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        stack.append(n-1)

        for i in range(n-2, -1, -1):
            while len(stack)!=0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if len(stack)!=0:
                res[i] = stack[-1] - i
            else:
                res[i] = 0

            stack.append(i)

        return res