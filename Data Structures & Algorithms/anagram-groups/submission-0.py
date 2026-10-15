class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map the character count to the list of anagrams
        # creation of dictionary where every new key starts with an empty list
        result = defaultdict(list)

        for s in strs:
            # create count array to hold amt of times a letter appears in a word
            count = [0] * 26 # a ... z

            for c in s:
                # convert each char a-z into an index from 0-25
                # += 1 increments frequency of the character
                count[ord(c) - ord("a")] += 1

            # add string s to the dictionary (as a corresponding value
            # to the key that tracks the specific arrangement of letters in a word)
            # in python - lists cannot be keys, so count shld be changed to tuple
            result[tuple(count)].append(s)

        return list(result.values())