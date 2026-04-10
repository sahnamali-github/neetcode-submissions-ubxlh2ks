class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        for n in s:
            countS[n] = 1 + countS.get(n, 0)
        for n in t:
            countT[n] = 1 + countT.get(n,0)
        return countS == countT
        