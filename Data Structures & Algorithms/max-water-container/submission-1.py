class Solution:
    def maxArea(self, heights: List[int]) -> int:
# Brute force Approach
        max_a = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if i !=j:
                    w = j - i
                    max_c = w * min(heights[i], heights[j])
                    max_a = max(max_a, max_c)
        return(max_a)
