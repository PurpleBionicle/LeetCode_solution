"""Given a signed 32-bit integer x, return x
with its digits reversed. If reversing x causes the value
 to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0."""


class Solution:
    def reverse(self, x: int) -> int:
        flag_negative = False if x >= 0 else True
        x = abs(x)
        x = int(str(x)[::-1])
        if flag_negative:
            x *= -1
        return x
