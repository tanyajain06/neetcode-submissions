class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # revisiting problem @ 1:10 AM 10/14

        # create set for the array nums
        seen = set()

        # iterate through nums and compare whether a val is in the set
        for i in nums:
            # is i in the set alr? --> duplication is what we are checking for
            if i in seen:
                return True
            # if i was not in the set yet, add it to set
            seen.add(i)
        return False