class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for n in nums:
                if n in curr:
                    continue
                curr.append(n)
                dfs(curr)
                curr.pop()
        dfs([])
        return res