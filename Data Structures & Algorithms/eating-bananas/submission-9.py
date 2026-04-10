class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        k = max(piles)
        while low <= high:
            res = 0
            mid = (low + high)//2
            for p in piles:
                res += (p+mid-1)//mid
            if res <= h:
                k = min(k, mid)
                high = mid - 1
            else:
                low = mid + 1
        return k


        # k = 1
        # while k <= max(piles):
        #     hours = 0
        #     for p in piles:
        #         hours += (p+k - 1) // k

        #     if hours <= h:
        #         return k
        #     k += 1



        # mink = max(piles)
        # smallk , largek = 1, max(piles)
        # while smallk <= largek:
        #     res = 0
        #     k = (smallk + largek) // 2
        #     for p in piles:

        #         res += (p + k - 1)//k
        #     if res <= h:
        #         mink = min(mink, k)
        #         largek = k - 1
        #     elif res > h:
        #         smallk = k + 1
        # return mink


