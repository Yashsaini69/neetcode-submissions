import math

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        product = [1] * n

        prefix = 1
        for i in range(n):
            product[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            product[i] = product[i] * suffix
            suffix = suffix * nums[i]   
        
        return product


solver = Solution()
nums = [1,2,4,6]

result = solver.productExceptSelf(nums)
print(result)

