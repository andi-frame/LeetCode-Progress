class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        longest_common_prefix = ""
        long_prefix = True
        for i in range(len(strs[0])):
            for str in strs[1:len(strs)]:
                try:
                    str[i]
                except:
                    return longest_common_prefix
                if strs[0][i] == str[i]:
                    long_prefix *= True
                else:
                    long_prefix *= False
            
            if long_prefix:
                longest_common_prefix += str[i]
        
        return longest_common_prefix
                


        """
        :type strs: List[str]
        :rtype: str
        """
