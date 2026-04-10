class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            height = heights[i]
            # extend left
            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            # extend right
            right = i
            while right < len(heights) and heights[right] >= height:
                right += 1
            width = right - left - 1
            area = height * width
            res = max(res,area)
        return res

        
            
        
        