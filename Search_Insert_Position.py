class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            try:
                if nums[i+1] >= target:
                    return i+1
            except:
                return i+1
