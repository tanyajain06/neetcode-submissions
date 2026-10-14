class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # set will not have any duplicates
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False