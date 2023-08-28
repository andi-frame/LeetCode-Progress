class Solution(object):
    def romanToInt(self, s):
        integer = 0
        roman_integer = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        i = 0
        while i < len(s):
            if i+1 < len(s):
                if s[i] == 'I' and s[i+1] == 'V':
                    integer += 4
                    i += 2
                    continue
                if s[i] == 'I' and s[i+1] == 'X':
                    integer += 9
                    i += 2
                    continue
                if s[i] == 'X' and s[i+1] == 'L':
                    integer += 40
                    i += 2
                    continue
                if s[i] == 'X' and s[i+1] == 'C':
                    integer += 90
                    i += 2
                    continue
                if s[i] == 'C' and s[i+1] == 'D':
                    integer += 400
                    i += 2
                    continue
                if s[i] == 'C' and s[i+1] == 'M':
                    integer += 900
                    i += 2
                    continue
            integer += roman_integer[s[i]]
            i +=1
        
        return integer


            

        """
        :type s: str
        :rtype: int
        """
