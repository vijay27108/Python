# Question 1 Given an integer x, return true if x is a palindrome, and false otherwise.
# class Solution():
#     def ispal(self, x):
#         if x<0:
#             False
#         x = str(x)
#         return x == x[::-1]
# sol = Solution()
# print(sol.ispal(121))
# print(sol.ispal(-123))

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# class Solution:
#     def isValid(self, s: str) -> bool:
#         bracket_map = {')': '(', '}': '{', ']': '['}
#         stack = []
#         for char in s:
#             if char in bracket_map:
#                 top_element = stack.pop() if stack else '#'
#                 if bracket_map[char] != top_element:
#                    return False
#             else:
#                 stack.append(char)
#         return not stack

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# def mySqrt(x):
#     if x == 0:
#         return 0
#     guess = x
#     while True:
#         next_guess = (guess + x // guess) // 2
#         if next_guess >= guess:
#             return guess
#         guess = next_guess

# print(mySqrt(8))



