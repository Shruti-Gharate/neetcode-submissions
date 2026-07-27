class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_ = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        for st in s:
            if st in '{([':
                stack.append(st)
            else:
                if not stack:
                    return False
                if stack[-1] != dict_[st]:
                    return False
                stack.pop()
        return len(stack) == 0