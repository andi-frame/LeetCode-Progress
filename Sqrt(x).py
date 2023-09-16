class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 2 or x == 3:
            return 1 
        if x == 0:
            return 0
        
        flag = False
        root = int(x/2)

        while True:
            if root**2 <= x:
                root = int(root + (root/2))
                flag = True
                continue
            else:
                if flag:
                    while root**2 > x:
                        root -= 1
                    return root
                root /= 2
