class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # coming back to this sol @ 12:58 AM 10/14

        # determine if string s and t len are equiv
        # if not, return false
        if len(s) != len(t):
            return False

        # create hashMaps for letters s and t
        # to hold the letters as keys
        # and the number of times each letter appears as vals

        countS, countT = {}, {}

        # assign each letter of s and t to the respective hashMap
        # can use len(s) because s and t have the same len

        # apply get func incase a specific letter is nonexistent in
        # the hashMap and this is the first time encountering that letter

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # compare the hashMaps of countS and countT (loop thru hashMaps)
        # and determine if the letters and frequency of letters align
        # if they do not match up, return false
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False
        return True
