class Solution:
    def maxArea(self, heights: List[int]) -> int:
       maxA = 0
       l, r = 0, len(heights) - 1
       while l < r:
        Area = (r - l)*(min(heights[r], heights[l]))
        maxA = max(Area,maxA)
        if heights[r] >= heights[l]:
            l += 1
        else:
            r -= 1
       return maxA