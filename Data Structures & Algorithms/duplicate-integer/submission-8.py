class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = set(nums)

        if (len(seen_set) !=len(nums)):
            return True
        else:
            return False