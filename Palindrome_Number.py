class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True

        """
        :type x: int
        :rtype: bool
        """
