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
                    z = y + x
                elif char == '-':
                    z = y - x
                elif char == '*':
                    z = x * y
                else:
                    z = int(y / x)
                stack.append(z)
            else:
                stack.append(char)

        return int(stack[-1])