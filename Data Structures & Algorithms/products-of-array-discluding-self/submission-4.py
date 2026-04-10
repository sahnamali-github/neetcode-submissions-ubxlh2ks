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
        # res = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             product *= nums[j]
        #     res.append(product)
        # return res

        # METHOD 3
        # n = len(nums)
        # pref,suff,res = [1]*n, [1]*n, [1] * n
        # pref[0] = 1
        # suff[n - 1] = 1
        # for i in range(1, n):
        #     pref[i] = nums[i - 1] * pref[i - 1]
        #     res[i] *= pref[i]
        # for i in range(n - 2, -1, -1):
        #     suff[i] = nums[i + 1] * suff[i + 1]
        #     res[i] *= suff[i]
        # return res

        # METHOD 4
        # res = [1] * len(nums)
        # prefix, postfix = 1, 1
        # for i in range(len(nums)):
        #     res[i] *= prefix
        #     prefix *= nums[i]
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res


        n = len(nums)
        res = [1] * n
        prefix, suffix = 1,1
        for i in range(1,n):
            prefix *= nums[i-1]
            res[i] *= prefix
        for i in range(n-2,-1,-1):
            suffix *= nums[i+1]
            res[i] *= suffix
        return res        
            

            

   
        




            
