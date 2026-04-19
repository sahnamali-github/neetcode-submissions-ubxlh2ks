class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        freq = [[] for i in range(len(nums)+1)]
        for keyz,valz in count.items():
            freq[valz].append(keyz)
        res = []
        for i in range(len(freq)-1,0,-1):
            for t in freq[i]:
                res.append(t)
                if len(res) == k:
                    return res

