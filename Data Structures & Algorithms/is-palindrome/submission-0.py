class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = s.lower()
        l, r = 0, len(snew) - 1
        while l<=r:
            while l < r and not self.isalpha(snew[l]):
                l += 1
            while r > l and not self.isalpha(snew[r]):
                r -= 1
            if snew[l] != snew[r]:
                return False
            l += 1
            r -= 1
        return True

    def isalpha(self,c):
        return ((ord("A")<=ord(c)<=ord("Z")) or (ord("a")<=ord(c)<=ord("z")) or (ord("0")<=ord(c)<=ord("9")))
              
            
                
            

                