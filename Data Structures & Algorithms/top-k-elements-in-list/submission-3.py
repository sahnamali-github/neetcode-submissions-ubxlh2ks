class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      for n in nums:
        count[n] = 1 + count.get(n, 0)
      pairs = []
      for keys, vals in count.items():
        pairs.append([keys,vals])
      pairs.sort(key = lambda x : x[1], reverse = True)
      res = []
      for i in range(len(pairs)):
        res.append(pairs[i][0])
        if len(res) == k:
            return res




    

     