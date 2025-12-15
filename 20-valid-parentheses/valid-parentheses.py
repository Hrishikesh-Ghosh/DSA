class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if stack and stack.pop() == mapping[ch]:
                    continue
                else:
                    return False
        return not stack