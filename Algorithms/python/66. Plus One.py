# Input: digits = [1,2,3]
# Output: [1,2,4]
from typing import List

digits = [1, 2, 3]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_list = [str(digit) for digit in digits]
        str_digit = ''.join(digits_list)
        int_digit = int(str_digit) + 1
        return [int(n) for n in str(int_digit)]


print(Solution().plusOne(digits))
