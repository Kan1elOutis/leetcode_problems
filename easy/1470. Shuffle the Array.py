# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution(object):
    def shuffle(self, nums, n):
        ts = []
        for i in range(n):
            ts += [nums[i]]
            ts += [nums[i + n]]
        return ts
