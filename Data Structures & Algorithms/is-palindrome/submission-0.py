class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initial sol
        newStr = ""
        for i in s:
            # adding only alphanumeric vals to newStr
            if i.isalnum():
                # keeping all lowercase
                newStr += i.lower()

        # checking if newStr is equivalent to it's reverse
        return newStr == newStr[::-1]
        