class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(m) for m in accounts)
                
        """
        :type accounts: List[List[int]]
        :rtype: int
        """