class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            result = width * height
            if result > best:
                best = result
            if height == heights[l]:
                l += 1
            elif height == heights[r]:
                r -= 1
        return best