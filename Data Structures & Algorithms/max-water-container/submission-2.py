class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        vol = 0
        while right > left:
            area = min(heights[left], heights[right]) * (right - left)
            vol = max(vol, area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -=1
        return vol

# Brute force Approach
"""        max_a = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if i !=j:
                    w = j - i
                    max_c = w * min(heights[i], heights[j])
                    max_a = max(max_a, max_c)
        return(max_a)
"""

