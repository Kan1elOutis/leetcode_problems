# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
# is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for
# which this is possible, keep answer[i] == 0 instead.


class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while (stack and stack[-1][0] < t):
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        return res
