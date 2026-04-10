class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset = set()
        # length = 0
        # L = 0
        # for R in range(len(s)):
        #     while s[R] in charset:
        #         charset.remove(s[L])
        #         L += 1
        #     charset.add(s[R])
        #     length = max(length, R-L+1)
        # return length
        count = 0
        myset = set()
        l = 0
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            count = max(count,r - l + 1)
        return count
        