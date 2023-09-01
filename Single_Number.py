class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            print("i", i)
            for j in nums[i:]:
                print("j", j)
                if nums[i] == j:
                    continue
