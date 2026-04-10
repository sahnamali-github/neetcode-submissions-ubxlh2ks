class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # METHOD 1
    #   count = {}
    #   for n in nums:
    #     count[n] = 1 + count.get(n, 0)
    #   pairs = []
    #   for keys, vals in count.items():
    #     pairs.append([keys,vals])
    #   pairs.sort(key = lambda x : x[1], reverse = True)
    #   res = []
    #   for i in range(len(pairs)):
    #     res.append(pairs[i][0])
    #     if len(res) == k:
    #         return res
        # METHOD 2 - BUCKET SORT
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res







    

     