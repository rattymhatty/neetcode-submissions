class Solution:
    def decodeString(self, s: str) -> str:
        currStr = ""
        currNum = 0
        stack = []
        for char in s:
            if char == '[':
                if not currNum:
                    raise ValueError("invalid input")
                stack.append(currStr)
                stack.append(currNum)
                currStr = ""
                currNum = 0
            elif char == ']':
                if len(stack) < 2:
                    raise ValueError("invalid input")
                repeat = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr * repeat
            elif '0' <= char <= '9':
                currNum = currNum * 10 + int(char)
            else:
                currStr += char
        if stack:
            raise ValueError("invalid input")
        return currStr