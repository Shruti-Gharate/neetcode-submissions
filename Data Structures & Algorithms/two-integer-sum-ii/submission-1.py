class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            c = numbers[left] + numbers[right]
            if c > target:
                right -= 1
            elif c < target:
                left += 1
            else:
                return [left+1, right+1]
"""
        seen = {}
        for i, num in enumerate(numbers):
            c = target - num
            if c in seen:
                return[seen[c] + 1, i + 1]
            seen[num] = i
"""