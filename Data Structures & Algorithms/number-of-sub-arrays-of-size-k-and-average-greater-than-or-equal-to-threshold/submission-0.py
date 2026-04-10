class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        for R in range(len(arr)):
            if R - L + 1 != k:
                continue
            avg = (sum(arr[L:R]) + arr[R]) // k
            if avg < threshold:
                L += 1
            else:
                res += 1
                L += 1
        return res
        