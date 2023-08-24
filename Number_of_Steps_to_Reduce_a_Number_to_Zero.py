class Solution(object):
    def numberOfSteps(self, num):
        step = 0
        while True:
            if num==0:
                break
            if num%2==1:
                num-=1
                step+=1
            else:
                num/=2
                step+=1
        return step

        """
        :type num: int
        :rtype: int
        """
