class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = {}
       for n in nums:
        count[n] = 1 + count.get(n, 0)
       arr = [[] for i in range(len(nums) + 1)]
       for key, val in count.items():
        arr[val].append(key)
       res = []
       for i in range(len(arr)-1, 0, -1):
        if arr[i]:
            for a in arr[i]:
                res.append(a)
                if len(res) == k:
                    return res

    

     