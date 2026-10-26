class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = {}

        if(nums == []):
            return 0

        for i in range(len(nums)):
            key = i
            sequence[key] = nums[i]

        sorted_sequence = sorted(sequence.items(), key=lambda item:item[1])

        values = []
        count = 1

        for i in range(len(sorted_sequence)-1):
            if(sorted_sequence[i+1][1] - sorted_sequence[i][1] == 1):
                count += 1

            elif(sorted_sequence[i+1][1] - sorted_sequence[i][1] > 1):
                values.append(count)
                count = 1

        values.append(count)
        values.sort(reverse = True)

        return values[0]

Answer = Solution()
nums = [2,20,4,10,3,4,5]

result = Answer.longestConsecutive(nums)
print(result)


