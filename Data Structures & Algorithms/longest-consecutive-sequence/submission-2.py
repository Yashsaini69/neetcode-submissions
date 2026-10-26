class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(nums == []):
            return 0

        nums.sort()

        values = []
        count = 1

        for i in range(len(nums)-1):
            if(nums[i+1] - nums[i] == 1):
                count += 1

            elif(nums[i+1] - nums[i] > 1):
                values.append(count)
                count = 1

        values.append(count)
        values.sort(reverse = True)

        return values[0]

Answer = Solution()
nums = [2,20,4,10,3,4,5]

result = Answer.longestConsecutive(nums)
print(result)


