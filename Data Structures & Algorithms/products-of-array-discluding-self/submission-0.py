class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        product = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n
        for i in range(len(nums)):
            # single zero
            if zero_count == 1:
                if nums[i] == 0:
                    res[i] = product
                else:
                    res[i] = 0
            # multiple zeroes
            elif zero_count > 1:
                res[i] = 0
            # no zeroes
            else:
                res[i] = product // nums[i]
        return res

            

   
        




            
