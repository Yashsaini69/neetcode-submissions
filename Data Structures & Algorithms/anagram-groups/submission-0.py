class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:
            key = "".join(sorted(word)) 

            if(key not in groups):
                groups[key] = []
                groups[key].append(word)

            else:
                groups[key].append(word)


        result = list(groups.values()) 

        return result                


Answer = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]

result = Answer.groupAnagrams(strs)

print(result)




        