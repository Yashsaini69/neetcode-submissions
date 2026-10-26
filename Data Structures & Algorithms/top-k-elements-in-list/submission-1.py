class Solution:
    def topKFrequent(self, nums, k):
        
        frequent = {}

        for i in range(len(nums)):
            key = nums[i]

            if(key not in frequent):
                frequent[key] = []
                frequent[key].append(nums[i])

            else:
                frequent[key].append(nums[i])    

        list = {}
        count = 0

        for key in frequent:
            count = len(frequent[key])
            list[key] = []
            list[key] = count
            
        sorted_list = sorted(list.items(), key=lambda item: item[-1], reverse=True)

        list_2 = []

        for i in range(k):
            list_2.append(sorted_list[i][0])

        return list_2

Answer = Solution()
nums = [1,2,2,3,3,3]
k = 2
result = Answer.topKFrequent(nums, 2)
print(result)        