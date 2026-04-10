class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # METHOD 1 
        # hashMap = defaultdict(list)
        # for s in strs:
        #     snew = sorted(s)
        #     hashMap[tuple(snew)].append(s)
        # return list(hashMap.values())
        # METHOD 2
        hashMap = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashMap[tuple(count)].append(s)
        return list(hashMap.values())

       
      
          