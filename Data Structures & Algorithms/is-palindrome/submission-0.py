class Solution:
    def isPalindrome(self, s):

        string = s.lower()
        string = "".join(char for char in string if char.isalnum())

        string_2 = "".join(reversed(string))

        count = 0
        for i in range(len(string)):
            if(string[i] == string_2[i]):
                count += 1
            else:
                return False

        return count == len(string)

Answer = Solution()
s = "Was it a car or a cat I saw?"
result = Answer.isPalindrome(s) 

print(result)