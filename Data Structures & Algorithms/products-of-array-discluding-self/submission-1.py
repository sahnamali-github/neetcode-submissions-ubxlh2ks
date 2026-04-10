class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # METHOD 1
        # res = []
        # product = 1
        # zero_count = 0
        # for n in nums:
        #     if n == 0:
        #         zero_count += 1
        #     else:
        #         product *= n
        # for i in range(len(nums)):
        #     # single zero
        #     if zero_count == 1:
        #         if nums[i] == 0:
        #             res.append(product)
        #         else:
        #             res.append(0)
        #     # multiple zeroes
        #     elif zero_count > 1:
        #         res.append(0)
        #     # no zeroes
        #     else:
        #         res.append(product//nums[i])
        # return res
        # METHOD 2
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            res.append(product)
        return res

            

   
        




            
