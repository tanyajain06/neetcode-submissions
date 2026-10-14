class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        # assign each letter in string s and t to a key and the 
        # amount of times the letter appears as the value

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # then compare each hashMap, and if the key and value differ
        # between countS and countT, return False

        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True