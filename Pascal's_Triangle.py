class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        after = [1,1]
        for i in range(1, numRows+1):
            if i == 1:
                pascal.append([1])
                continue
            elif i == 2:
                pascal.append([1,1])
                continue

            for j in range(i-2):
                after.insert(-1, (pascal[i-2][j] + pascal[i-2][j+1]))
                
            pascal.append(after)
            after = [1,1]

        return pascal
