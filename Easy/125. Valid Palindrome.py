# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution(object):
    def isPalindrome(self, s):
        list = [i.lower() for i in s]
        list = [ord(i.lower()) for i in list if ord(i) in range(97, 122) or ord(i) in range(48, 58)]
        return True if list == list[::-1] else False
