class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k-1
        while r < len(nums):
            length = nums[l:r+1]
            res.append(max(length))
            l += 1
            r += 1
        return res
        