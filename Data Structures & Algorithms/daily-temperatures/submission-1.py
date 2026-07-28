class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                h = stack.pop()
                res[h] = i - h
            stack.append(i)
        return res

        #Brute Force
"""
        list = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
            list.append(count)
        return list
"""