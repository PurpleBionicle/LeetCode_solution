"""Backspace String Compare"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while s.count('#') != 0:
            i = s.index('#')
            if i != 0:
                s = s[:i - 1] + s[i + 1:]
            else:
                t = t[:i - 1] + t[i + 1:]

        while t.count('#') != 0:
            i = t.index('#')
            if i != 0:
                t = t[:i - 1] + t[i + 1:]
            else:
                t = t[:i] + t[i + 1:]

        return s == t