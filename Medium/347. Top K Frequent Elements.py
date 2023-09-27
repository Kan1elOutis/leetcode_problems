# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution(object):
    def topKFrequent(self, nums, k):
        d = dict.fromkeys(set(nums), 0)
        sorted_dict = {}
        for num in nums:
            d[num] += 1
        sorted_keys = sorted(d, key=d.get)
        return sorted_keys[:-k - 1:-1]
