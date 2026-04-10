class Solution:
    def trap(self, height: List[int]) -> int:
        premax = [0]*len(height)
        for i in range(len(height)):
            premax[i]+=(max(max(premax),height[i]))
        postmax=[0]*len(height)
        for i in range(len(height)-1,-1,-1):
            postmax[i]+=(max(max(postmax),height[i]))
        res = 0
        for i in range(len(height)):
            res += min(premax[i], postmax[i])-height[i]
        return res

       