class Solution:
    def isAnagram(self, s, t):
        if(len(s) != len(t)):
            return False

        hash_list_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        hash_list_2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        for i in range(len(s)):   
            ascii_val = ord(s[i])
            index = ascii_val - 97
            hash_list_1[index] += 1

        for j in range(len(t)):
            ascii_val = ord(t[j])
            index = ascii_val - 97
            hash_list_2[index] += 1 

        #comparing hash arays of both strings

        return hash_list_1 == hash_list_2

    
solver = Solution()
s = "aabcs"
t = "aabcc"

result = solver.isAnagram(s,t)

if(result == True):
    print("Both s and t string are anagram of each other")

else:
    print("string are not anagram of each other")