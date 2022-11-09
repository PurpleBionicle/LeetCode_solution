"""Backspace String Compare"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def new_str(s: str) -> list:
            res = []

            for i in s:
                if i != '#':
                    res.append(i)
                elif res:
                    res.pop()
            return res

        return new_str(s) == new_str(t)