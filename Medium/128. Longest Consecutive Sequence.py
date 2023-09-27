# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                lenght = 1
                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(lenght, longest)
        return longest
