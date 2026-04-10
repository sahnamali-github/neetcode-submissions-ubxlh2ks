class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # METHOD 1
    #   copyN = [[n,i] for i, n in enumerate(nums)]
    #   copyN.sort()
    #   l, r = 0, len(nums) - 1
    #   while l < r:
    #     if copyN[l][0] + copyN[r][0] < target:
    #         l += 1
    #     elif copyN[l][0] + copyN[r][0] > target:
    #         r -= 1
    #     else:
    #         return [copyN[l][1], copyN[r][1]]
        # METHOD 2
        hashMap = {}
        for i , n in enumerate (nums):
            if target - n not in hashMap:
                hashMap[n] = i
            else:
                return [hashMap[target - n], i]


        