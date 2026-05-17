class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        prev=None
        for i in nums:
            if prev!=None and prev==i:
                return True
            prev=i
        return False
        