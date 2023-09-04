class Solution:

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            bit = 0
            if i == 0:
                ans.append(i)
                continue
            while i/2 != 0:
                if i%2==1:
                    bit += 1
                    i -= 1
                    i /= 2
                else:
                    i /= 2

            ans.append(bit)

        return ans
        
