class Solution(object):
    def maximumWealth(self, accounts):
        max = 0
        for m in accounts:
            sum = 0
            for n in m:
                sum += n
            m = sum
            if m > max:
                max = m
        return max
                
        """
        :type accounts: List[List[int]]
        :rtype: int
        """