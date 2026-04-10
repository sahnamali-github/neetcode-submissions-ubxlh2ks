class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        for n in nums1:
            res.append(n)
        for n in nums2:
            res.append(n)
        res.sort()
        l, r = 0, len(res) - 1
        mid = (l + r) // 2
        if len(res) % 2 != 0:
            return res[mid]
        else:
            return ((res[mid] + res[mid + 1])/ 2)

        