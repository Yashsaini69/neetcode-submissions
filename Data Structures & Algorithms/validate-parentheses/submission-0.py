class Solution:
    def __init__(self):
        self.list = []

    def push(self, open_bracket):
        self.list.insert(0, open_bracket)

    def check_match(self, expected_open):
        if len(self.list) == 0:
            return False

        if self.list[0] == expected_open:
            self.list.pop(0)
            return True
        else:
            return False

    # NeetCode strictly calls this exact method name and passes `s` here
    def isValid(self, s: str) -> bool:
        self.list = []  # Reset the list for every new test case
        symbols = {
            1: "(",
            2: "[",
            3: "{"
        }

        for i in s:
            if i == "[" or i == "(" or i == "{":
                self.push(i)

            elif i == "]" or i == ")" or i == "}":
                if i == ")":
                    matched = self.check_match(symbols[1])
                elif i == "]":
                    matched = self.check_match(symbols[2])
                elif i == "}":
                    matched = self.check_match(symbols[3])

                if not matched:
                    return False

        return len(self.list) == 0