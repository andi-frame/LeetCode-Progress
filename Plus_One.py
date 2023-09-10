class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            before = digits.index(digits[-1]-1, 0, len(digits))
            n = before[-1]
            
            for i in range(len(digits)-1,-1,-1):
                digits[i] = 0
            digits.insert(0, 1)
            return digits

        digits[-1] += 1

        return digits
