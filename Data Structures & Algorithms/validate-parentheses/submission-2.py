class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != pairing[ch]:
                    return False
                stack.pop()
        return len(stack) == 0