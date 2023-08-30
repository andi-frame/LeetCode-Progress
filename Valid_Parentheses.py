class Solution(object):
    def isValid(self, s):
        memory = []
        num = len(s)
        for c in s:
            if c in "([{":
                memory.append(c)
                num -= 1
            if not memory or len(s)%2 != 0:
                return False
            if (c == ')' and memory[-1] == '(') or (c == ']' and memory[-1] == '[') or (c == '}' and memory[-1] == '{'):
                memory.pop()
                num -= 1
      
        if num == 0 and len(memory) == 0:
            return True
        else:
            return False


        """
        :type s: str
        :rtype: bool
        """
