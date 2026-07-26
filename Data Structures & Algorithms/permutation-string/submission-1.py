from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]
            left += 1
            if window == target:
                return True
        return False