class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            height = heights[i]
            left = i
            while left >=0 and heights[left] >= height:
                left -= 1
            right = i
            while right < len(heights) and heights[right] >= height:
                right += 1
            res = max((right-left-1) * height, res )
        return res