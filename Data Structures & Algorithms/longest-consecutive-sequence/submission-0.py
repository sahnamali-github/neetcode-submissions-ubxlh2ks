class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for n in (nums):
            if (n - 1) not in nums:
                count = 1
                while (n+1) in nums:
                    n += 1
                    count += 1
            max_count = max(count,max_count)
        return max_count

        
        
       
        






        