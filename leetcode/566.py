from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if self.canReshape(mat, r, c):
            reshapedMat = []

            elements = iter(self.getElements(mat))

            for row in range(r):
                reshapedRow = []
                for _ in range(c):
                    reshapedRow.append(elements.__next__())

                reshapedMat.append(reshapedRow)

            return reshapedMat

        else:
            return mat

    def canReshape(self, mat: List[List[int]], r: int, c: int) -> int:

        rowCount = 0

        for row in mat:
            rowCount += 1
            colCount = 0
            for _ in row:
                colCount += 1

        return rowCount*colCount == r*c

    def getElements(self, mat: List[List[int]]) -> List[int]:
        arr = []

        for row in mat:
            for v in row:
                arr.append(v)

        return arr


mat = [[1, 2], [3, 4]]
r = 2
c = 2
print(Solution().matrixReshape(mat, r, c))
