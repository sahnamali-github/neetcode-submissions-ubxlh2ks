class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = 1
        # while k <= max(piles):
        #     hours = 0
        #     for p in piles:
        #         hours += (p+k - 1) // k

        #     if hours <= h:
        #         return k
        #     k += 1
        mink = max(piles)
        smallk , largek = 1, max(piles)
        while smallk <= largek:
            res = 0
            k = (smallk + largek) // 2
            for p in piles:

                res += (p + k - 1)//k
            if res <= h:
                mink = min(mink, k)
                largek = k - 1
            elif res > h:
                smallk = k + 1
        return mink


