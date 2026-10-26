class Solution:
    def twoSum(self, nums, target):
        
        target_elements = []

        j = 0

        for i in range(len(nums)):
            for j in range(len(nums)-1, 0, -1):
                if(j > i):
                    if(nums[i] + nums[j] == target):
                        target_elements.append(i)
                        target_elements.append(j)
                    

        return target_elements
        


solver = Solution()

nums = [3,4,5,6]
target = 7

elements = []
elements.append(solver.twoSum(nums, target))

print(elements)
