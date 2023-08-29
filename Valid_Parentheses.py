class Solution(object):
    def isValid(self, s):
        memory = []
        for c in s:
            if c in "([{":
                memory.append(c)
            if not memory or len(s)%2 != 0:
                return False
            if (c == ')' and memory[-1] == '(') or (c == ']' and memory[-1] == '[') or (c == '}' and memory[-1] == '{'):
                memory.pop()
      
        if len(memory) == 0:
            return True
        else:
            return False


        """
        :type s: str
        :rtype: bool
        """
