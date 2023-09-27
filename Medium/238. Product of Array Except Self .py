# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        post_prefix = 0
        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
                post_prefix = 1
            else:
                post_prefix *= nums[i - 1]
                answer.append(post_prefix)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                post_prefix = 1
            else:
                print(post_prefix)
                post_prefix *= nums[i + 1]
                answer[i] *= post_prefix
        return answer
