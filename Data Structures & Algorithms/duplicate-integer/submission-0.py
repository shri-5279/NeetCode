class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new=[]
        for x in nums:
            if x in new:
                return True
            else:
                new.append(x)
        return False