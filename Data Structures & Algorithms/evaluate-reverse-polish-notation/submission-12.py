class Solution:
    def evalRPN(self, tokens: List[str]) -> int:      
        stack = []

        for char in tokens:
            if char in '+-*/':
                x = int(stack[-1])
                stack.pop()
                y = int(stack[-1])
                stack.pop()
                if char == '+':
                    x = y + x
                elif char == '-':
                    x = y - x
                elif char == '*':
                    x = x * y
                else:
                    x = int(y / x)
                stack.append(x)
            else:
                stack.append(char)

        return int(stack[-1])