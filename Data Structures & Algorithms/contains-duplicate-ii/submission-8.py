class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False

        # window = set()
        # L = 0
        # for R in range(len(nums)):
            
        #     if R - L > k:
        #         window.remove(nums[L])
        #         L += 1
        #     if L != R and nums[R] in window and ((R-L) <=k):
        #         return True
        #     window.add(nums[R])
        # return False

        window = set()
        L = 0
        for R in range(len(nums)):
            if nums[R] in window:
                return True
            window.add(nums[R])
            if R - L >= k:
                window.remove(nums[L])
                L += 1
        return False



                


        
        