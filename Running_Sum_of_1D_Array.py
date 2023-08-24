class Solution(object):
    def runningSum(self, nums):
        result = []
        num = int()
        for i in range(len(nums)):
            for j in range(0, i+1):
                num += nums[j]
            result.append(num)
            num = 0
        return result
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
