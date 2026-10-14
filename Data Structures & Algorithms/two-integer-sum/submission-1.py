class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashMap to track all keys (number) / values (index)
        # using a hashMap to refer nums and indices that have alr been checked
        prevMap = {}

        # enumerate --> creates keys and values
        # i --> index
        # n --> value @ index
        for i, n in enumerate(nums):
            # checking for a value that will add with n to equal target
            diff = target - n
            # currently on n
            # check if diff in prevMap, if not then add n to prevMap
            # doing this bc if diff in prevMap, you can end process early (solution)
            if diff in prevMap:
                # return answer with smaller index first
                # prevMap[diff] --> index of diff within prevMap
                # i --> currently the index we are on (that matches w diff)
                return [prevMap[diff], i]
            # this is how you set key, value pair in hashMap
            # setting the n value to the index i
            prevMap[n] = i
        # this line is not reached but just a precaution "in case no sol was there"
        return