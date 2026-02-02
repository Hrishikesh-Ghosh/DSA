class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i == ")":
                if stack and stack.pop() == "(":
                    continue
                else:
                    return False
            elif i == "}":
                if stack and stack.pop() == "{":
                    continue
                else:
                    return False
            elif i == "]":
                if stack and stack.pop() == "[":
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
            