class Solution:
    def findMin(self, nums: List[int]) -> int:
        # METHOD 1
        # l, r = 0, len(nums) - 1
        # if len(nums) == 1:
        #         return nums[0]
        # while l <= r:
        #     if nums[l] > nums[r] and nums[r] > nums[r - 1]:
        #         r -= 1
        #     elif nums[l] > nums[r] and nums[r] < nums[r - 1]:
        #         return nums[r]
        #     elif nums[l] < nums[r]:
        #         return nums[l]
        #     else:
        #         l += 1
        # return -1

        # METHOD 2
        mnm = nums[0]
        for n in nums:
            if n < mnm:
                mnm = n
        return mnm

        