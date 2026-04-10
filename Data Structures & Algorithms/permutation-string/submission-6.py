class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1, counts2 = [0]*26, [0]*26
        for i in range(len(s1)):
            counts1[ord(s1[i])-ord("a")] += 1
        L = 0
        for R in range(len(s2)):
            if counts1[ord(s2[R])-ord("a")] == 0:
                L = R + 1
                counts2 = [0]*26
            else: 
                counts2[ord(s2[R])-ord("a")] += 1
            while counts2[ord(s2[R])-ord("a")] > counts1[ord(s2[R])-ord("a")]:
                counts2[ord(s2[L])-ord("a")] -= 1
                L += 1
            if (R-L+1) == len(s1) and counts1 == counts2:
                return True
        return False

        