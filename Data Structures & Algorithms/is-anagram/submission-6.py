class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # METHOD 1
    #   return sorted(s) == sorted(t)
        # METHOD 2
        # if len(s) != len(t):
        #     return False
        # countS, countT = {}, {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT
        # METHOD 3
        if len(s) != len(t):
            return False
            
        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True
    

            

  