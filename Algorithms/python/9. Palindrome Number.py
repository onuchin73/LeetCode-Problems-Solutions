# Input: x = 121
# Output: true
#
# Input: x = -121
# Output: false

x = 121


# 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        number = x
        reverse = 0
        while (number > 0):
            y = number % 10
            number = number // 10
            reverse = reverse * 10 + y
        return reverse == x


print(Solution().isPalindrome(x))

# 2 convert to str
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]
#
#
# print(Solution().isPalindrome(x))


# 3 convert to str
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         rev = ''.join(reversed(str(x)))
#         if rev == str(x):
#             return True
#         else:
#             return False


# print(Solution().isPalindrome(x))
