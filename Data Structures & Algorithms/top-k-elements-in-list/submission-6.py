class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for keyz,valz in count.items():
            freq[valz].append(keyz)
        res = []
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                for n in freq[i]:
                    res.append(n)
                    if len(res) ==k:
                        return res


