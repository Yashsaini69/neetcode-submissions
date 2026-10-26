class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for i in range(len(nums)):
            key = nums[i]

            if(key not in duplicate):
                duplicate[key] = []

            else:
                duplicate[key].append(i)    

        for key in duplicate:        
            if(duplicate[key] != []):
                return True

        return False                 


answer = Solution()
nums = [1,2,3,4,4]

result = answer.hasDuplicate(nums)

print(result)