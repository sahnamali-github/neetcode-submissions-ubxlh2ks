class Solution:
    def trap(self, height: List[int]) -> int:
        premax = [0]*len(height)
        for i in range(1,len(height)):
            premax[i] =(max(premax[i-1],height[i-1]))
        postmax=[0]*len(height)
        for i in range(len(height)-2,-1,-1):
            postmax[i] = (max(height[i+1],postmax[i+1]))
        res = 0
        for i in range(len(height)):
            if height[i] > min(premax[i], postmax[i]):
                continue
            else:
                res += min(premax[i], postmax[i]) - height[i]
        return res

       