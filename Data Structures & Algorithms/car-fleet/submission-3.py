class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed),reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        #Brute Force
"""
        seen = set()
        fleets = 0
        for i in range(len(position)):
            x = int((target - position[i]) / speed[i])
            seen.add(x)
        return len(seen)
"""