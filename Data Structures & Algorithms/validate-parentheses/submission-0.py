class Solution:
    def isValid(self, s: str) -> bool:
        c = {'(', '[', '{'}
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in c:
                stack.append(char)
            elif char in d:
                if not stack or stack.pop() != d[char]:
                    return False
        return len(stack) == 0