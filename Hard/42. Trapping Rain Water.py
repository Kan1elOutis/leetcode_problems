# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water it can trap after raining.
class Solution:
    def trap(self, height):
        if not height:
            return 0

        res = 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res
