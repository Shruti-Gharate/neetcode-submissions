class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = []
        nums_s = sorted(nums)
        for i in range(len(nums_s) - 2):
            if i > 0 and nums_s[i] == nums_s[i-1]:
                continue
            left = i + 1
            right = len(nums_s) - 1
            while left < right:
                total = nums_s[i] + nums_s[left] + nums_s[right]
                if total == 0:
                    seen.append([nums_s[i], nums_s[left], nums_s[right]])
                    left += 1
                    right -= 1
                    while left < right and nums_s[left] == nums_s[left - 1]:
                        left += 1
                    while left < right and nums_s[right] == nums_s[right + 1]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return seen

# Making use of a set here, as it's simple or sort and compare due to suage of hash function &
# then converting that sorted and compared set to a list! 
# List takes (n) whereas set takes O(1).
"""        seen = set()
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)): 
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_set = tuple(sorted([nums[i], nums[j], nums[k]]))
                        seen.add(sorted_set)
        return [list(t) for t in seen]
"""