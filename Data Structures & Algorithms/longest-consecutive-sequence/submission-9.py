class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_l = 0

        for num in seen:
            if num - 1 not in seen:
                current = num
                length = 1

                while current + 1 in seen:
                    current += 1
                    length += 1

                max_l = max(max_l, length)

        return max_l